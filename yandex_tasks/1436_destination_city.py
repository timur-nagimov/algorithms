class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph_dict = {}

        for path in paths:
            from_point, to_point = path
            if from_point not in graph_dict:
                graph_dict[from_point] = []
            graph_dict[from_point].append(to_point)

        for key, value in graph_dict.items():
            for to_point in value:
                if to_point not in graph_dict:
                    return to_point
