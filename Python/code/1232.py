class solution:
    def checkStraightLine(self, coordinates):
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        one_line = True
        for i in range(2,len(coordinates)):
            x3,y3 = coordinates[i]
            if not (x2-x1)*(y3-y1)==(x3-x1)*(y2-y1):
                one_line = False
        return one_line

if __name__ == '__main__':
    sol = solution()
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(sol.checkStraightLine(coordinates))
