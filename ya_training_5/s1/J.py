import threading
import io
w = 0
h = 0
c = 0


class MyImage:
    STYLE_EMBEDDED = 0
    STYLE_FLOATING = 1
    STYLE_SURROUNDED = 2

    def __init__(self):
        self.height = 0
        self.width = 0
        self.dx = 0
        self.dy = 0
        self.style = 0
        self.x = 0
        self.y = 0
        self.text = False

    def set_style(self, value):
        if value == "surrounded":
            self.style = MyImage.STYLE_SURROUNDED
        elif value == "floating":
            self.style = MyImage.STYLE_FLOATING
        elif value == "embedded":
            self.style = MyImage.STYLE_EMBEDDED


class MyReader:
    def __init__(self, reader):
        self.in_file = reader if isinstance(
            reader, io.TextIOBase) else io.StringIO(reader)
        self.text = []
        self.cur_paragraph = 0

        str_list = []
        sb = []
        for line in self.in_file:
            line = line.strip()
            if len(line) == 0:
                if sb:  # РџСЂРѕРІРµСЂСЏРµРј, РµСЃС‚СЊ Р»Рё С‡С‚Рѕ-С‚Рѕ РІ Р±СѓС„РµСЂРµ РїРµСЂРµРґ РґРѕР±Р°РІР»РµРЅРёРµРј
                    str_list.append(''.join(sb))
                    sb = []
                continue

            sb.append(' ')
            sb.append(line)

        if sb:  # РџСЂРѕРІРµСЂСЏРµРј Р±СѓС„РµСЂ РїРѕСЃР»Рµ РѕРєРѕРЅС‡Р°РЅРёСЏ С†РёРєР»Р°
            str_list.append(''.join(sb))

        self.text = [list(s) for s in str_list]

    def next_paragraph(self):
        if self.cur_paragraph >= len(self.text):
            return None

        images = []
        str_chars = self.text[self.cur_paragraph]
        self.cur_paragraph += 1
        cur = 0

        while cur < len(str_chars):
            if str_chars[cur].isspace():
                cur += 1
                continue
            if str_chars[cur] == '(':
                from_index = cur + 1
                cur += 1  # РџРµСЂРµРјРµС‰Р°РµРјСЃСЏ Р·Р° РѕС‚РєСЂС‹РІР°СЋС‰СѓСЋ СЃРєРѕР±РєСѓ
                while cur < len(str_chars) and str_chars[cur] != ')':
                    cur += 1
                # РџСЂРѕРІРµСЂСЏРµРј РЅР° СЃР»СѓС‡Р°Р№, РµСЃР»Рё Р·Р°РєСЂС‹РІР°СЋС‰Р°СЏ СЃРєРѕР±РєР° РѕС‚СЃСѓС‚СЃС‚РІСѓРµС‚
                if cur >= len(str_chars):
                    break
                to = cur
                cur += 1  # РџРµСЂРµРјРµС‰Р°РµРјСЃСЏ Р·Р° Р·Р°РєСЂС‹РІР°СЋС‰СѓСЋ СЃРєРѕР±РєСѓ

                info = str_chars[from_index:to]
                info_str = ''.join(info)
                info_str = info_str.replace("image ", "").replace("=", " ")
                fields = info_str.split()

                image = MyImage()
                for i in range(0, len(fields), 2):
                    field = fields[i].strip()
                    value = fields[i + 1].strip()

                    if field == "layout":
                        image.set_style(value)
                    elif field == "dx":
                        image.dx = int(value)
                    elif field == "dy":
                        image.dy = int(value)
                    elif field == "width":
                        image.width = int(value)
                    elif field == "height":
                        image.height = int(value)

                images.append(image)
                continue

            size = 0
            while cur < len(str_chars) and str_chars[cur] != '(' and not str_chars[cur].isspace():
                cur += 1
                size += 1

            image = MyImage()
            image.text = True
            image.set_style("embedded")
            image.width = size * c
            image.height = h
            images.append(image)

        return images

    def close(self):
        self.in_file.close()


class MyDocument:
    def __init__(self):
        self.start_position = 0

    def add_paragraph(self, images):
        cur_position = 0
        cur_height_pos = self.start_position
        cur_height = h

        need_white_space = False
        for i, cur_image in enumerate(images):

            if cur_image.style == MyImage.STYLE_FLOATING:
                if i > 0 and images[i - 1].style == MyImage.STYLE_FLOATING:
                    cur_image.y = images[i - 1].y + cur_image.dy
                    cur_image.x = max(
                        min(images[i - 1].x + images[i - 1].width + cur_image.dx, w - cur_image.width), 0)
                    continue
                cur_image.y = cur_height_pos + cur_image.dy
                cur_image.x = max(
                    min(cur_position + cur_image.dx, w - cur_image.width), 0)
                continue

            while True:
                new_pos = w
                left = w
                width = cur_image.width
                if cur_image.style == MyImage.STYLE_EMBEDDED and need_white_space:
                    width += c

                for j in range(i):
                    img = images[j]
                    if img.style == MyImage.STYLE_SURROUNDED and img.y + img.height > cur_height_pos and img.x >= cur_position:
                        if img.x < left:
                            left = img.x
                            new_pos = img.x + img.width

                if cur_position + width <= left:
                    break

                cur_position = new_pos
                need_white_space = False
                if cur_position == w:
                    cur_position = 0
                    cur_height_pos += cur_height
                    cur_height = h

            if cur_image.style == MyImage.STYLE_EMBEDDED and need_white_space:
                cur_image.x = cur_position + c
            else:
                cur_image.x = cur_position

            cur_image.y = cur_height_pos
            need_white_space = False
            if cur_image.style == MyImage.STYLE_EMBEDDED:
                cur_height = max(cur_height, cur_image.height)
                need_white_space = True

            cur_position = cur_image.width + cur_image.x

        if images:
            self.start_position = cur_height_pos + cur_height
        else:
            self.start_position = cur_height_pos

        for img in images:
            if img.style == MyImage.STYLE_SURROUNDED:
                self.start_position = max(
                    self.start_position, img.y + img.height)


def solve():
    global w, h, c

    # Чтение из файла input.txt
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Извлечение параметров w, h и c
    w, h, c = map(int, lines[0].split())

    # Инициализация reader с оставшимися строками, исключая первую
    in_reader = MyReader(''.join(lines[1:]))
    doc = MyDocument()

    all_images = []
    while True:
        cur = in_reader.next_paragraph()
        if cur is None:
            break

        for image in cur:
            all_images.append(image)
        doc.add_paragraph(cur)

    # Запись в файл output.txt
    with open('output.txt', 'w') as file:
        for image in all_images:
            if not image.text:
                file.write(f"{image.x} {image.y}\n")


def main():
    solve()


if __name__ == "__main__":
    main()
