class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        y_dict = {}
        # Добавляем точки в словарь в следующем виде
        # y: [x`ы на этой координате]
        for point in points:
            x, y = point
            if y not in y_dict:
                y_dict[y] = set()
            y_dict[y].add(x)

        line_min = line_max = None
        line = None
        for y, x_values in y_dict.items():
            # задаем линию между двумя точками
            if line is None:
                line_min = min(x_values)
                line_max = max(x_values)
                line = (line_min + line_max) / 2

            # Смотрим, для всех ли точек можно провести линию
            while x_values:
                # берем случайную точку
                x = x_values.pop()
                dist_to_opposite = abs(x-line)
                # высчитываем точку, которая должна быть с другой стороны
                opposite_x = None
                if x > line:
                    opposite_x = line - dist_to_opposite
                elif x < line:
                    opposite_x = line + dist_to_opposite
                else:
                    # пропускаем, т.к для точки на линии не нужна другая
                    continue

                if opposite_x not in x_values:
                    return False
                # также удаляем противоположную точку
                x_values.remove(opposite_x)

        return True
