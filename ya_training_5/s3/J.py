class Device:
    all_devices = []
    global_updates = []

    def __init__(self, total_updates, num_devices):
        self.is_updated = [False] * total_updates
        self.scores = [0] * num_devices
        self.pending_requests = []
        self.total_updates_done = 0
        self.required_update = -1
        self.total_iterations = 0
        self.id = len(Device.all_devices)
        self.is_request_approved = False
        self.approver_id = -1
        Device.all_devices.append(self)

    def select_and_request_update(self):
        self.required_update = -1
        least_updates = float('inf')
        for idx, updated in enumerate(self.is_updated):
            if not updated and Device.global_updates[idx] < least_updates:
                least_updates = Device.global_updates[idx]
                self.required_update = idx
        if self.required_update != -1:
            self.total_iterations += 1
            self.search_for_approver()

    def search_for_approver(self):
        if self.required_update == -1:
            return
        least_updates = float('inf')
        approver = None
        for device in Device.all_devices:
            if device.is_updated[self.required_update] and device.total_updates_done < least_updates:
                approver = device
                least_updates = device.total_updates_done
        if approver:
            approver.pending_requests.append(self)

    def process_and_fulfill_requests(self):
        if not self.pending_requests:
            return
        chosen_device_id = -1
        highest_score = -1
        least_updates = float('inf')
        for request in self.pending_requests:
            if self.scores[request.id] > highest_score or \
               (self.scores[request.id] == highest_score and request.total_updates_done < least_updates):
                chosen_device_id = request.id
                least_updates = request.total_updates_done
                highest_score = self.scores[request.id]
        self.pending_requests.clear()
        if chosen_device_id != -1:
            Device.all_devices[chosen_device_id].is_request_approved = True
            Device.all_devices[chosen_device_id].approver_id = self.id

    def fulfill_request(self):
        if not self.is_request_approved:
            return
        self.total_updates_done += 1
        self.is_updated[self.required_update] = True
        Device.global_updates[self.required_update] += 1
        self.scores[self.approver_id] += 1
        self.is_request_approved = False


def make_decision(num_devices, total_updates):
    Device.all_devices = []
    Device.global_updates = [1] * total_updates
    for _ in range(num_devices):
        Device(total_updates, num_devices)
    Device.all_devices[0].total_updates_done = total_updates
    Device.all_devices[0].is_updated = [True] * total_updates

    while True:
        all_done = sum(device.total_updates_done ==
                       total_updates for device in Device.all_devices)
        if all_done == num_devices:
            break

        for device in Device.all_devices:
            if device.total_updates_done < total_updates:
                device.select_and_request_update()

        for device in Device.all_devices:
            device.process_and_fulfill_requests()

        for device in Device.all_devices:
            device.fulfill_request()

    return [device.total_iterations for device in Device.all_devices[1:]]


def main():
    n, k = map(int, input().split())
    result = make_decision(n, k)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
