import random



class Cube:
    
    top = [["W","W","W"], ["W","W","W"], ["W","W","W"]]
    bottom = [["G","Y","Y"], ["Y","Y","Y"], ["R","Y","Y"]]
    front = [["G","G","G"], ["G","G","G"], ["R","G","B"]]
    left = [["O","O","O"], ["O","O","O"], ["O","O","G"]]
    right = [["R","R","R"], ["R","R","R"], ["Y","R","Y"]]
    back = [["B","B","B"], ["B","B","B"], ["O","B","B"]]
    
    solution_moves = [["Scrambling rotations:"],["White Cross:"],["White Corners:"],["Second Layer:"],["Yellow Cross:"],["Yellow Edges:"],
                          ["Yellow Corners:"],["Final Step:"], ["Trash: "]]
    
    #functions to create a fresh cube, display cube, and record solution rotations
    
    def fresh_cube(self):
        
        for i in range(0,3):
            for j in range(0,3):
                self.top[i][j] = "W"
                self.front[i][j] = "G"
                self.bottom[i][j] = "Y"
                self.left[i][j] = "O"
                self.right[i][j] = "R"
                self.back[i][j] = "B"
    
    def display(self):
        for i in range(0,3):
            print("\t\t  ",self.top[i])
        print()

        for i in range(0,3):
            print(self.left[i],"  ",self.front[i],"  ",self.right[i],"  ",self.back[i])  
        print()

        
        for i in range(0,3):
            print("\t\t  ", self.bottom[i])
        print()
        print()
        
        
    
    def record_solution(self,step,move):
        
        self.solution_moves[step].append(move)
    
    def show_solution(self):
        
        for i in range(0,8):
            print(self.solution_moves[i])
        print()    
        
    #building block functions for cube rotation functions
    
    def transpose(face):
        for i in range(len(face)):
            for j in range(i+1, len(face)):
                face[i][j], face[j][i] = face[j][i], face[i][j]
        
    def reverse_face_columns(face):
        face.reverse()            
    
    def reverse_column(face, column):
        face[0][column], face[2][column] = face[2][column], face[0][column]
    
    def reverse_face_rows(face):
        for row in range(0,3):
            face[row].reverse()    

    def reverse_row(face, column):
        face[column].reverse()
    
    def rotate_90(self,face):
        self.transpose(face)
        self.reverse_face_rows(face)
        
    def rotate_90p(self,face):
        self.transpose(face)
        self.reverse_face_columns(face)

    def rotate_180(self,face):
        self.reverse_face_rows(face)
        self.reverse_face_columns(face)
    
    #functions to move around the cube as you would irl (turn it left, right, flip it upside down, etc..)
    
    def flip(self,step):
        self.rotate_180(self,self.front)
        self.rotate_180(self,self.back)
        self.rotate_180(self,self.left)
        self.rotate_180(self,self.right)
        
        self.top, self.bottom = self.bottom, self.top
        self.left, self.right = self.right, self.left
        
        self.record_solution(self,step,"flip")
    
    def turn_left(self,step):
        self.back, self.left = self.left, self.back
        self.front, self.right = self.right, self.front
        self.right, self.left = self.left, self.right
        
        self.rotate_90(self,self.top)
        self.rotate_90p(self,self.bottom)
        
        self.record_solution(self,step,"<---")
    
    def turn_right(self,step):
        self.left, self.right = self.right, self.left
        self.right, self.front = self.front, self.right
        self.left, self.back = self.back, self.left
        
        self.rotate_90p(self,self.top)
        self.rotate_90(self,self.bottom)
        
        self.record_solution(self,step,"--->")
    
    def bottom_front(self,step):
        self.back, self.bottom = self.bottom, self.back
        self.top, self.front = self.front, self.top
        self.back, self.front = self.front, self.back
        
        self.rotate_90p(self, self.left)
        self.rotate_90(self, self.right)
        self.reverse_face_columns(self.back)
        self.reverse_face_columns(self.front)
        self.reverse_face_rows(self.back)
        self.reverse_face_rows(self.front)
        
        self.record_solution(self,step,"|^|")
    
    def green_front(self,step):
        
        while not self.front[1][1] == "G":
            self.turn_right(self,8)
        
        self.record_solution(self,step,"[G]")
    
    def orange_front(self,step):
        
        while not self.front[1][1] == "O":
            self.turn_right(self,8)
            
        self.record_solution(self,step,"[O]")
    
    def blue_front(self,step):
        
        while not self.front[1][1] == "B":
            self.turn_right(self,8)
        
        self.record_solution(self,step,"[B]")
    
    def red_front(self,step):
        
        while not self.front[1][1] == "R":
            self.turn_right(self,8)
        
        self.record_solution(self,step,"[R]")
            
    #functions for the basic cube row and column rotations
    
    def F(self,step,switch):
        self.rotate_90(self,self.front)
        
        for i in range(0, 3):
            self.left[i][2], self.right[i][0] = self.right[i][0], self.left[i][2]
            self.right[i][0], self.top[2][i] = self.top[2][i], self.right[i][0]
            self.left[i][2], self.bottom[2][i] = self.bottom[2][i], self.left[i][2]
        
          
        self.reverse_row(self.top,2)
        self.reverse_column(self.left,2)
        
        if switch == "Yes":
            self.record_solution(self,step,"F")
    
    def Fp(self,step,switch):
        self.rotate_90p(self,self.front)
        
        for i in range(0, 3):
            self.bottom[2][i], self.left[i][2] = self.left[i][2], self.bottom[2][i]
            self.top[2][i], self.right[i][0] = self.right[i][0], self.top[2][i]
            self.right[i][0], self.left[i][2] = self.left[i][2], self.right[i][0]
        
         
        self.reverse_row(self.bottom,2)
        self.reverse_column(self.left,2)
        if switch == "Yes":
            self.record_solution(self,step,"Fp")
    
    def R(self,step,switch):
        self.rotate_90(self, self.right)
        
        for i in range(0, 3):
            self.bottom[i][0], self.top[i][2] = self.top[i][2], self.bottom[i][0]
            self.top[i][2], self.front[i][2] = self.front[i][2], self.top[i][2]
            self.bottom[i][0], self.back[i][0] = self.back[i][0], self.bottom[i][0]
        
        self.reverse_column(self.front,2)
        self.reverse_column(self.back,0)
        if switch == "Yes":
            self.record_solution(self,step,"R")   
    
    def Rp(self,step,switch):
        self.rotate_90p(self,self.right)
        
        for i in range(0,3):
            self.back[i][0], self.bottom[i][0] = self.bottom[i][0], self.back[i][0]
            self.front[i][2], self.top[i][2] = self.top[i][2], self.front[i][2]
            self.top[i][2], self.bottom[i][0] = self.bottom[i][0], self.top[i][2]
        
        self.reverse_column(self.top,2)
        self.reverse_column(self.bottom,0)
        if switch == "Yes":
            self.record_solution(self,step,"Rp")
    
    def U(self,step,switch):
        self.rotate_90(self, self.top)
        
        for i in range(0,3):
            self.back[0][i], self.left[0][i] = self.left[0][i], self.back[0][i]
            self.front[0][i], self.right[0][i] = self.right[0][i], self.front[0][i]
            self.right[0][i], self.left[0][i] = self.left[0][i], self.right[0][i]
        if switch == "Yes":
            self.record_solution(self,step,"U")    
    
    def Up(self,step,switch):
        self.rotate_90p(self,self.top)
        
        for i in range(0,3):
            self.left[0][i], self.right[0][i] = self.right[0][i], self.left[0][i]
            self.right[0][i], self.front[0][i] = self.front[0][i], self.right[0][i]
            self.left[0][i], self.back[0][i] = self.back[0][i], self.left[0][i]
        
        if switch == "Yes":
            self.record_solution(self,step,"Up")
    
    def L(self,step,switch):
        self.rotate_90(self,self.left)
        
        for i in range(0,3):
            self.back[i][2], self.bottom[i][2] = self.bottom[i][2], self.back[i][2]
            self.front[i][0], self.top[i][0] = self.top[i][0], self.front[i][0]
            self.top[i][0], self.bottom[i][2] = self.bottom[i][2], self.top[i][0]
            
        self.reverse_column(self.top,0)
        self.reverse_column(self.bottom,2)
        if switch == "Yes":
            self.record_solution(self,step,"L")
    
    def Lp(self,step,switch):
        self.rotate_90p(self,self.left)
        
        for i in range(0,3):
            self.bottom[i][2], self.top[i][0] = self.top[i][0], self.bottom[i][2]
            self.top[i][0], self.front[i][0] = self.front[i][0], self.top[i][0]
            self.bottom[i][2], self.back[i][2] = self.back[i][2], self.bottom[i][2]
        
        self.reverse_column(self.front,0)
        self.reverse_column(self.back,2)
        if switch == "Yes":
            self.record_solution(self,step,"Lp")
    
    def D(self,step,switch):
        self.rotate_90(self,self.bottom)
        
        for i in range(0,3):
            self.left[2][i], self.right[2][i] = self.right[2][i], self.left[2][i]
            self.right[2][i], self.front[2][i] = self.front[2][i], self.right[2][i]
            self.left[2][i], self.back[2][i] = self.back[2][i], self.left[2][i]
        
        if switch == "Yes":
            self.record_solution(self,step,"D")
    
    def Dp(self,step,switch):
        self.rotate_90p(self,self.bottom)
        
        for i in range(0,3):
            self.back[2][i], self.left[2][i] = self.left[2][i], self.back[2][i]
            self.front[2][i], self.right[2][i] = self.right[2][i], self.front[2][i]
            self.right[2][i], self.left[2][i] = self.left[2][i], self.right[2][i]
        
        if switch == "Yes":
            self.record_solution(self,step,"Dp")
    
    def right_shimmy(self,step):
        self.R(self,step,"no")
        self.U(self,step,"no")
        self.Rp(self,step,"no")
        self.Up(self,step,"no")
        
        self.record_solution(self,step,"r-shim")
    
    def left_shimmy(self,step):
        self.Lp(self,step,"no")
        self.Up(self,step,"no")
        self.L(self,step,"no")
        self.U(self,step,"no")

        self.record_solution(self,step,"l-shim")
    
    def pop_piece_left(self,step):
        
        self.Up(self,step,"Yes")
        self.left_shimmy(self,step)
        self.turn_right(self,step)
        self.right_shimmy(self,step)
        self.turn_left(self,step)
        
    def pop_piece_right(self,step):
        
        self.U(self,step,"Yes")
        self.right_shimmy(self,step)
        self.turn_left(self,step)
        self.left_shimmy(self,step)
        self.turn_right(self,step)
    
    # Function for scrambling cube
    
    def scramble(self):
        
        moves = [random.randint(1,10)]
        for i in range(1,20):
            moves.append(random.randint(1,10))
            
            while moves[i] == moves[i-1]:
                moves.insert(i,random.randint(1,10))

        for i in range(0,20):
            
            if moves[i] == 1:
                self.F(self,0,"Yes")
            elif moves[i] == 2:
                self.Fp(self,0,"Yes")
            elif moves[i] == 3:
                self.R(self,0,"Yes")
            elif moves[i] == 4:
                self.Rp(self,0,"Yes")
            elif moves[i] == 5:
                self.U(self,0,"Yes")
            elif moves[i] == 6:
                self.Up(self,0,"Yes")
            elif moves[i] == 7:
                self.L(self,0,"Yes")
            elif moves[i] == 8:
                self.Lp(self,0,"Yes")
            elif moves[i] == 9:
                self.D(self,0,"Yes")
            else:
                self.Dp(self,0,"Yes")
   
   #all function for White Cross
    
    def scan_top(self):
        
        pieces = 0
        
        if self.top[0][1] == "W":
            pieces += 1
        if self.top[1][2] == "W":
            pieces += 1
        if self.top[2][1] == "W":
            pieces += 1
        if self.top[1][0] == "W":
            pieces += 1
        
        return pieces
    
    def scan_adj(self):
        
        if((self.front[0][1] == self.front[1][1]) and (self.left[0][1] == self.left[1][1]) and (self.right[0][1] == self.right[1][1]) and (self.back[0][1] == self.back[1][1])):
            return True
        else:
            return False
    
    def middle_cross_check(self):
        
        self.green_front(self,1)
        
        while self.bottom[0][1] != "W" or self.bottom[1][2] != "W" or self.bottom[2][1] != "W" or self.bottom[1][0] != "W":
            
            if self.top[2][1] == "W":
                while self.bottom[2][1] == "W":
                    self.D(self,1,"Yes")
                self.F(self,1,"Yes")
                self.F(self,1,"Yes")
            
            if self.front[1][0] == "W":
                while self.bottom[1][2] == "W":
                    self.D(self,1,"Yes")
                self.L(self,1,"Yes")
            
            if self.front[1][2] == "W":
                while self.bottom[1][0] == "W":
                    self.D(self,1,"Yes")
                self.Rp(self,1,"Yes")
            
            if self.front[2][1] == "W":
                while self.bottom[2][1] == "W":
                    self.D(self,1,"Yes")
                self.Fp(self,1,"Yes")
                
                while self.bottom[1][0] == "W":
                    self.D(self,1,"Yes")
                self.Rp(self,1,"Yes")
            
            if self.front[0][1] == "W":
                while self.bottom[2][1] == "W":
                    self.D(self,1,"Yes")
                self.Fp(self,1,"Yes")
                
                while self.bottom[1][2] == "W":
                    self.D(self,1,"Yes")
                self.L(self,1,"Yes")
            
            else:
                self.turn_right(self,1)
        
        self.green_front(self,1)
    
    def set_cross(self):
        
        while self.top[0][1] != "W" or self.top[1][0] != "W" or self.top[2][1] != "W" or self.top[1][2] != "W":
            while self.front[1][1] != self.front[2][1] or self.bottom[2][1] != "W":
                self.D(self,1,"Yes")
            self.F(self,1,"Yes")
            self.F(self,1,"Yes")
            self.turn_right(self,1)
        self.green_front(self,1)
    
    def cross_to_bottom(self):
        
        for i in range(0,4):
            if self.top[2][1] == "W":
                while self.bottom[2][1] == "W":
                    self.D(self,1,"Yes")
                self.F(self,1,"Yes")
                self.F(self,1,"Yes")
            else:
                self.turn_right(self,1)
            
    def white_cross(self):
        
        if((self.scan_top(self) == 4) and (self.scan_adj(self) == True)):
            print("Go buy a lottery ticket, white cross is already done!")
        
        elif((self.scan_top(self) == 4) and (self.scan_adj(self) == False)):
            print("White cross is on top but adjacent pieces do not match")
            self.green_front(self,1)
            self.cross_to_bottom(self)
            print("Pieces moved to bottom, shifting to final position")
            self.set_cross(self)
            print("White cross complete :)")
        
        elif((self.scan_top(self) < 4) and (self.scan_top(self) != 0)):
            print(self.scan_top(self), " white on top")
            self.green_front(self,1)
            self.cross_to_bottom(self)
            print("Pieces moved to bottom")
            print("Processing middle section")
            self.middle_cross_check(self)
            print("All white pieces moved to bottom, shifting to final position")
            self.set_cross(self)
            print("White Cross Complete :)")
        
        else:
            print("No white pieces on the top, processing middle")
            self.middle_cross_check(self)
            print("All white pieces moved to bottom, shifting to final position")
            self.set_cross(self)
            print("White Cross Complete :)")
    
    #all functions for White Corners
    
    def bottom_corners_check(self):
        
        status = False
        if ((self.bottom[0][0] == "W") and (self.bottom[0][2] == "W") and (self.bottom[2][0] == "W") and (self.bottom[2][2] == "W")):
            status = True
        
        return status
    
    def adj_corners_check(self):
        
        position = False
        
        if ((self.front[2][2] == self.front[1][1]) and (self.front[2][0] == self.front[1][1]) and (self.right[2][2] == self.right[1][1]) and (self.right[2][0] == self.right[1][1]) 
            and (self.left[2][2] == self.left[1][1]) and (self.left[2][0] == self.left[1][1]) and (self.back[2][2] == self.back[1][1]) and (self.back[2][0] == self.back[1][1])):
            
            position = True
        
        return position
    
    def scan_corners(self,color1,color2):
        
        if ((self.front[2][2] == color1) and (self.bottom[2][0] == "W") and (self.right[2][0] == color2)):
            return "final position"
        
        elif ((self.front[0][2] == "W" or self.front[0][2] == color1 or self.front[0][2] == color2)
              and (self.top[2][2] == "W" or self.top[2][2] == color1 or self.top[2][2] == color2)
              and (self.right[0][0] == "W" or self.right[0][0] == color1 or self.right[0][0] == color2)):
            
            return "top right"
        
        elif ((self.front[2][2] == "W" or self.front[2][2] == color1 or self.front[2][2] == color2)
              and (self.bottom[2][0] == "W" or self.bottom[2][0] == color1 or self.bottom[2][0] == color2)
              and (self.right[2][0] == "W" or self.right[2][0] == color1 or self.right[2][0] == color2)):
            
            return "bottom right"
        
        elif ((self.front[0][0] == "W" or self.front[0][0] == color1 or self.front[0][0] == color2)
              and (self.top[2][0] == "W" or self.top[2][0] == color1 or self.top[2][0] == color2)
              and (self.left[0][2] == "W" or self.left[0][2] == color1 or self.left[0][2] == color2)):
            
            return "top left"
        
        elif ((self.front[2][0] == "W" or self.front[2][0] == color1 or self.front[2][0] == color2)
              and (self.bottom[2][2] == "W" or self.bottom[2][2] == color1 or self.bottom[2][2] == color2)
              and (self.left[2][2] == "W" or self.left[2][2] == color1 or self.left[2][2] == color2)):
            
            return "bottom left"
        
        else:
            return "not here"
    
    def white_corners(self):
        
        self.green_front(self,2)
        self.flip(self,2)
        
        print("Beginning White Corners")
        
        while ((self.bottom_corners_check(self) == False) or (self.adj_corners_check(self) == False)):
            
            color1 = self.front[1][1]
            color2 = self.right[1][1]
            
            if (self.scan_corners(self,color1,color2) == "final position"):
                print("This corner has already been set, moving on")
                self.turn_right(self,2)
            
            elif (self.scan_corners(self,color1,color2) == "top right"):
                print("piece found on top right")
                
                while (self.scan_corners(self,color1,color2) != "final position"):
                    self.right_shimmy(self,2)
                
                print("corner set")
                self.turn_right(self,2)
            
            elif (self.scan_corners(self,color1,color2) == "bottom right"):
                print("piece found on bottom right")
                
                while (self.scan_corners(self,color1,color2) != "final position"):
                    self.right_shimmy(self,2)
                
                print("corner set")
                self.turn_right(self,2)
            
            elif (self.scan_corners(self,color1,color2) == "top left"):
                print("piece found on top left")
                self.Up(self,2,"Yes")
                
                while (self.scan_corners(self,color1,color2) != "final position"):
                    self.right_shimmy(self,2)
                
                print("corner set")
                self.turn_right(self,2)
            
            elif (self.scan_corners(self,color1,color2) == "bottom left"):
                print("piece found on bottom left")
                self.left_shimmy(self,2)
                self.Up(self,2,"Yes")
                
                while (self.scan_corners(self,color1,color2) != "final position"):
                    self.right_shimmy(self,2)
                
                print("corner set")
                self.turn_right(self,2)
                
            elif (self.scan_corners(self,color1,color2) == "not here"):
                print("piece was not found in this face, searching the others")
                turns = 1
                self.turn_right(self,2)
                
                while (self.scan_corners(self,color1,color2) == "not here"):
                    self.turn_right(self,2)
                    turns += 1
                
                if ((self.scan_corners(self,color1,color2) == "top left") or (self.scan_corners(self,color1,color2) == "top right")):
                    print("piece was found on the top left or right of a different face")
                    
                    for i in range(0,turns):
                        self.turn_left(self,2)
                    
                    while (self.scan_corners(self,color1,color2) != "top right"):
                        self.Up(self,2,"Yes")
                    
                elif(self.scan_corners(self,color1,color2) == "bottom left"):
                    print("piece was found on the bottom left of a different face")
                    self.left_shimmy(self,2)
                    
                    for i in range(0,turns):
                        self.turn_left(self,2)
                    
                    while (self.scan_corners(self,color1,color2) != "top right"):
                        self.Up(self,2,"Yes")
                
                elif(self.scan_corners(self,color1,color2) == "bottom right"):
                    print("piece was found on the bottom left of a different face")
                    self.right_shimmy(self,2)
                    
                    for i in range(0,turns):
                        self.turn_left(self,2)
                    
                    while (self.scan_corners(self,color1,color2) != "top right"):
                        self.Up(self,2,"Yes")
                
                while (self.scan_corners(self,color1,color2) != "final position"):
                    self.right_shimmy(self,2)
                
                print("corner set")
                self.turn_right(self,2)
            
    #all functions for Second Layer
    
    def scan_side_pieces(self,color1,color2):
        
        if (self.front[1][2] == color1 and self.right[1][0] == color2):
            
            return "final position"
        
        elif (self.front[1][2] == color2 and self.right[1][0] == color1):
            
            return "right middle"
        
        elif (self.front[0][1] == color1 and self.top[2][1] == color2):
            
            return "top middle matching front"
        
        elif (self.front[0][1] == color2 and self.top[2][1] == color1):
            
            return "top middle matching right"
        
        elif ((self.front[1][0] == color1 or self.front[1][0] == color2) and (self.left[1][2] == color1 or self.left[1][2] == color2)):
            
            return "left middle"
        
        else:
            
            return "not here"
        
    def side_pieces_check(self):
        
        if ((self.front[1][1] == self.front[1][2] and self.front[1][1] == self.front[1][0]) and (self.left[1][1] == self.left[1][2] and self.left[1][1] == self.left[1][0])
            and (self.right[1][1] == self.right[1][2] and self.right[1][1] == self.right[1][0]) and (self.back[1][1] == self.back[1][2] and self.back[1][1] == self.back[1][0])):
            
            return True
        else:
            return False
        
    def second_layer(self):
        
        self.green_front(self,3)
        print("Beginning Second Layer")
        
        while(self.side_pieces_check(self) == False):
            
            color1 = self.front[1][1]
            color2 = self.right[1][1]
            
            if (self.scan_side_pieces(self,color1,color2) == "final position"):
                
                print("this piece is already set, moving to the next face")
                self.turn_right(self,3)
            
            elif (self.scan_side_pieces(self,color1,color2) == "right middle"):
                
                print("the piece is in its final position, but the colors are switched. Fixing now")
                self.pop_piece_right(self,3)
                self.U(self,3,"Yes")
                self.pop_piece_right(self,3)
                print("piece set, moving to next face")
                self.turn_right(self,3)
            
            elif (self.scan_side_pieces(self,color1,color2) == "top middle matching front"):
                
                print("the piece is in the top middle and matches the front face, setting now")
                self.pop_piece_right(self,3)
                print("piece set, moving to next face")
                self.turn_right(self,3)
            
            elif (self.scan_side_pieces(self,color1,color2) == "top middle matching right"):
                
                print("the piece is in the top middle and matches the right face, setting now")
                self.turn_left(self,3)
                self.Up(self,3,"Yes")
                self.pop_piece_left(self,3)
                print("piece set, moving to next face")
                self.turn_right(self,3)
            
            elif (self.scan_side_pieces(self,color1,color2) == "left middle"):
                
                print("the piece is in the left middle, popping it out now")
                self.pop_piece_left(self,3)
                self.Up(self,3,"Yes")
                print("piece popped, setting now")
                self.pop_piece_right(self,3)
                print("piece set, moving to next face")
                self.turn_right(self,3)
            
            elif (self.scan_side_pieces(self,color1,color2) == "not here"):
                
                print("the piece we need is not on this face, searching others")
                turns = 1
                self.turn_right(self,3)
                
                while (self.scan_side_pieces(self,color1,color2) == "not here"):
                    
                    self.turn_right(self,3)
                    turns += 1
                
                if (self.scan_side_pieces(self,color1,color2) == "top middle matching front"):
                    
                    print("piece was found in the top middle of a different face and matches the front, bringing it back now")
                    for i in range(0,turns):
                        self.turn_left(self,3)
                        self.Up(self,3,"Yes")
                    print("piece brought back, setting into final position")
                    self.pop_piece_right(self,3)
                    self.turn_right(self,3)
                    
                elif (self.scan_side_pieces(self,color1,color2) == "top middle matching right"):
                    
                    print("piece was found in the top middle of a different face and matches the right, bringing it back now")
                    for i in range(0,turns):
                        self.turn_left(self,3)
                        self.Up(self,3,"Yes")
                    print("piece brought back, setting into final position")
                    self.turn_left(self,3)
                    self.Up(self,3,"Yes")
                    self.pop_piece_left(self,3)
                    self.turn_right(self,3)
                    self.turn_right(self,3)
                
                elif (self.scan_side_pieces(self,color1,color2) == "left middle"):
                    
                    print("piece was found in the left middle of a different face, popping and bringing it back now")
                    self.pop_piece_left(self,3)
                    self.Up(self,3,"Yes")
                    
                    for i in range(0,turns):
                        self.turn_left(self,3)
                        self.Up(self,3,"Yes")
                    print("piece brought back, setting into final position")
                    
                    if (self.scan_side_pieces(self,color1,color2) == "top middle matching front"):
                        self.pop_piece_right(self,3)
                    else:
                        self.turn_left(self,3)
                        self.Up(self,3,"Yes")
                        self.pop_piece_left(self,3)
                        self.turn_right(self,3)
                    
                    self.turn_right(self,3)
        
        print("Second Layer Complete!")
    
    #all functions for Yellow Cross
    
    def scan_yellow_cross(self, color1):
        
        if (self.top[0][1] == color1 and self.top[1][0] == color1 and self.top[2][1] == color1 and self.top[1][2] == color1):
            return "cross complete"
        
        elif (self.top[0][1] == color1 and self.top[1][1] == color1 and self.top[2][1] == color1):
            return "line not set"
        
        elif ((self.top[1][0] == color1 and self.top[1][1] == color1 and self.top[2][1] == color1) or
              (self.top[0][1] == color1 and self.top[1][1] == color1 and self.top[1][2] == color1) or 
              (self.top[2][1] == color1 and self.top[1][1] == color1 and self.top[1][2] == color1)):
            return "L-shape not set"
    
    def yellow_cross(self):
        
        self.green_front(self,4)
        print("Beginning Yellow Cross")
        
        topcolor = self.top[1][1]
        
        while (self.scan_yellow_cross(self,topcolor) != "cross complete"):
            
            if (self.scan_yellow_cross(self,topcolor) == "L-shape not set"):
                
                print("l-shape found, setting now")
                while (self.top[1][0] != topcolor or self.top[0][1] != topcolor):
                    self.U(self,4,"Yes")
                print("l-shape set")
            
            elif (self.scan_yellow_cross(self,topcolor) == "line not set"):
                print("vertical line found, shifting horizontal")
                self.U(self,4,"Yes")
                print("line set")
            
            self.F(self,4,"Yes")
            self.right_shimmy(self,4)
            self.Fp(self,4,"Yes")
        
        print("Yellow Cross Complete")
    
    #all functions for Yellow Edges
    
    #                          color1,color2,color3,color4
    def scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor):
        
        if (self.front[0][1] == self.front[1][1] and self.right[0][1] == self.right[1][1] and self.back[0][1] == self.back[1][1]):
            return "yellow edges complete"
        
        elif ((self.front[0][1] == rcolor and self.right[0][1] == bcolor and self.back[0][1] == lcolor and self.left[0][1] == fcolor) or
              (self.front[0][1] == bcolor and self.right[0][1] == lcolor and self.back[0][1] == fcolor and self.left[0][1] == rcolor) or
              (self.front[0][1] == lcolor and self.right[0][1] == fcolor and self.back[0][1] == rcolor and self.left[0][1] == bcolor)):
            
            return "edges set but not matched"
        
        elif ((self.left[0][1] == fcolor and self.front[0][1] == rcolor) or (self.back[0][1] == fcolor and self.left[0][1] == rcolor) or (self.right[0][1] == fcolor and self.back[0][1] == rcolor)):
            
            return "front right L not matched"
        
        elif (self.front[0][1] == fcolor and self.right[0][1] == rcolor):
            return "front right L matched"
        
        elif ((self.front[0][1] == rcolor and self.right[0][1] == bcolor) or (self.left[0][1] == rcolor and self.front[0][1] == bcolor) or (self.back[0][1] == rcolor and self.left[0][1] == bcolor)):
            return "right back L not matched"
        
        elif(self.right[0][1] == rcolor and self.back[0][1] == bcolor):
            return "right back L matched"
        
        elif ((self.right[0][1] == bcolor and self.back[0][1] == lcolor) or (self.front[0][1] == bcolor and self.right[0][1] == lcolor) or (self.left[0][1] == bcolor and self.front[0][1] == lcolor)):               
            return "back left L not matched"
        
        elif (self.back[0][1] == bcolor and self.left[0][1] == lcolor):
            return "back left L matched"
        
        elif ((self.back[0][1] == lcolor and self.left[0][1] == fcolor) or (self.right[0][1] == lcolor and self.back[0][1] == fcolor) or (self.front[0][1] == lcolor and self.right[0][1] == fcolor)):
            return "front left L not matched"
        
        elif (self.front[0][1] == fcolor and self.left[0][1] == lcolor):
            return "front left L matched"
        
        elif ((self.left[0][1] == fcolor and self.right[0][1] == bcolor) or (self.back[0][1] == fcolor and self.front[0][1] == bcolor) or (self.right[0][1] == fcolor and self.left[0][1] == bcolor)):
            return "opposite front back not set"
        
        elif (self.front[0][1] == fcolor and self.back[0][1] == bcolor):
            return "opposite front back set"
        
        elif ((self.front[0][1] == rcolor and self.back[0][1] == lcolor) or (self.left[0][1] == rcolor and self.right[0][1] == lcolor) or (self.back[0][1] == rcolor and self.front[0][1] == lcolor)):
            return "opposite right left not set"
        
        elif (self.right[0][1] == rcolor and self.left[0][1] == lcolor):
            return "opposite right left set"
    
    def set_yellow_edges(self):
        
        self.R(self,5,"no")
        self.U(self,5,"no")
        self.Rp(self,5,"no")
        self.U(self,5,"no")
        self.R(self,5,"no")
        self.Up(self,5,"no")
        self.Up(self,5,"no")
        self.Rp(self,5,"no")
        
        self.record_solution(self,5,"SYE")
            
    def yellow_edges(self):
        
        self.green_front(self,5)
        fcolor, rcolor, bcolor, lcolor = self.front[1][1], self.right[1][1], self.back[1][1], self.left[1][1]
        print("Beginning Yellow Edges")
        
        while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) != "yellow edges complete"):
            
            if (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "edges set but not matched"):
                print("yellow edges set but not matched, positioning now")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "edges set but not matched"):
                    self.U(self,5,"Yes")
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "front right L not matched"):
                print("front right matching, setting into place")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "front right L not matched"):
                    self.U(self,5,"Yes")
                print("front right set, positioning")
                self.turn_right(self,5)
                print("front right positioned, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "front right L matched"):
                print("front right already set, positioning now")
                self.turn_right(self,5)
                print("front right positioned, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "right back L not matched"):
                print("right back matching, setting into place")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "right back L not matched"):
                    self.U(self,5,"Yes")
                print("right back set, performing rotation")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "right back L matched"):
                print("right back already set, performing rotation")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "back left L not matched"):
                print("back left matching, setting into place")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "back left L not matched"):
                    self.U(self,5,"Yes")
                print("back left set, positioning now")
                self.turn_left(self,5)
                print("back left positioned, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "back left L matched"):
                print("back left already set, positioning now")
                self.turn_left(self,5)
                print("back left positioned, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "front left L not matched"):
                print("front left matching, setting into place")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "front left L not matched"):
                    self.U(self,5,"Yes")
                print("front left set, positioning now")
                self.turn_left(self,5)
                self.turn_left(self,5)
                print("front left positioned, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "front left L matched"):
                print("front left already set, positioning now")
                self.turn_left(self,5)
                self.turn_left(self,5)
                print("front left positioned, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "opposite front back not set"):
                print("front back opposite matching, setting into place")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "opposite front back not set"):
                    self.U(self,5,"Yes")
                print("front back opposite set, positioning now")
                self.turn_right(self,5)
                print("front back opposite positioned, performing rotation")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "opposite front back set"):
                print("front back opposite already set, positioning now")
                self.turn_right(self,5)
                print("front back opposite positioned, performing rotation")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "opposite right left not set"):
                print("right left opposite matching, setting into place")
                while (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "opposite right left not set"):
                    self.U(self,5,"Yes")
                print("right left opposite set, performing rotations")
                self.set_yellow_edges(self)
            
            elif (self.scan_yellow_edges(self,fcolor,rcolor,bcolor,lcolor) == "opposite right left set"):
                print("right left opposite already set, performing rotation")
                self.set_yellow_edges(self)
        
        print("Yellow Edges Complete")

    #all functions for Yellow Corners
    
    def position_yellow_corners(self):
        
        if ((self.front[0][2] == self.front[1][1] or self.front[0][2] == self.top[1][1] or self.front[0][2] == self.right[1][1]) and
            (self.top[2][2] == self.front[1][1] or self.top[2][2] == self.top[1][1] or self.top[2][2] == self.right[1][1]) and
            (self.right[0][0] == self.front[1][1] or self.right[0][0] == self.top[1][1] or self.right[0][0] == self.right[1][1])):
            
            return "corner match"
    
    def scan_yellow_corners(self):
        
        matches = 0
        
        for i in range(0,4):
            if ((self.front[0][2] == self.front[1][1] or self.front[0][2] == self.top[1][1] or self.front[0][2] == self.right[1][1]) and
                (self.top[2][2] == self.front[1][1] or self.top[2][2] == self.top[1][1] or self.top[2][2] == self.right[1][1]) and
                (self.right[0][0] == self.front[1][1] or self.right[0][0] == self.top[1][1] or self.right[0][0] == self.right[1][1])):
                
                matches += 1
            self.turn_right(self,8)
            
        return matches
    
    def set_yellow_corners(self):
        
        self.U(self,6,"no")
        self.R(self,6,"no")
        self.Up(self,6,"no")
        self.Lp(self,6,"no")
        self.U(self,6,"no")
        self.Rp(self,6,"no")
        self.Up(self,6,"no")
        self.L(self,6,"no")
        
        self.record_solution(self,6,"SYC")
    
    def yellow_corners(self):
        
        self.green_front(self,6)
        print("Beginning Yellow Corners")
        
        while(self.scan_yellow_corners(self) != 4):
            if (self.scan_yellow_corners(self) == 0):
                self.set_yellow_corners(self)
                
            elif (self.scan_yellow_corners(self) in range(1, 4)):
                while (self.position_yellow_corners(self) != "corner match"):
                    self.turn_right(self,6)
                self.set_yellow_corners(self)
            
        print("Yellow Corners Complete")    
    
    #all functions for Final Step
    
    def final_step(self):
        
        self.green_front(self,7)
        self.flip(self,7)
        print("Beginning Final Step")
        
        if (self.bottom[2][0] == self.bottom[1][1] and self.bottom[2][2] == self.bottom[1][1] and self.bottom[0][0] == self.bottom[1][1] and self.bottom[0][2] == self.bottom[1][1]):
            print("Congrats! Cube is already complete")
        
        else:
            
            for i in range(0,4):
                
                while (self.bottom[2][0] != self.bottom[1][1]):
                    self.right_shimmy(self,7)
                self.D(self,7,"Yes")
            
            print("Cube Complete :)")
            
    
        