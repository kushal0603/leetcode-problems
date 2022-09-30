class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key = lambda k: (k[0], -k[2])) # by left (asc), then by height (desc)
        buildings.append([float('inf'), float('inf'), 0]) # to help with end condition
        height_mxheap = [] # [(height, right), ...]
        skyline = [] # [(left, height), ...]

        for left, right, height in buildings:

            # while max height building has been passed
            while height_mxheap and height_mxheap[0][1] <= left:

                _, last_right = heapq.heappop(height_mxheap)

                if last_right == left: # has alredy been accounted for
                    continue

                # pop all shorter heights with a right that passed before last_right
                while height_mxheap and height_mxheap[0][1] <= last_right:
                    heapq.heappop(height_mxheap)

                if height_mxheap: # if there is something left, end the previous section and add this
                    if skyline[-1][1] != -height_mxheap[0][0]:
                        skyline.append([last_right, -height_mxheap[0][0]])
                else: # if there is nothing, add a 0 section
                    skyline.append([last_right, 0])

            heapq.heappush(height_mxheap, (-height, right))

            max_height = -height_mxheap[0][0]
			# start next section with current max height building
            if not skyline or skyline[-1][1] != max_height:
                skyline.append([left, max_height])

        return skyline