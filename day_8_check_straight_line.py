class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        first_coordinate = coordinates[0]
        second_coordinate = coordinates[1]
        delta_y = second_coordinate[1] - first_coordinate[1]

        delta_x = second_coordinate[0] -  first_coordinate[0]

        
        initial_slope = delta_y / delta_x if delta_x else 0
        
        for coordinate in coordinates[1:]:
            current_delta_y = coordinate[1] - first_coordinate[1]
            current_delta_x = coordinate[0] - first_coordinate[0]

            current_slope = current_delta_y / current_delta_x if current_delta_x else 0
            
            if current_slope != initial_slope:
                return False
        
        return True
