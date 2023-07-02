class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        n = len(coordinates)

        if n<=2:
            return True

        else :
            if (coordinates[1][0] - coordinates[0][0]) != 0:
                m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
            else:
                m = 1e9

            for i in range(0,n-1):
                m1 = 1e9
                if (coordinates[i+1][0] - coordinates[i][0]) !=0:
                    m1 = (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0])

                if m1 != m:
                    return False

            return True
