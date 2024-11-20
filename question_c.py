import random

class generate_question:
    def __init__(self, point):
        self.point = point
        self.answer = None

    def create(self):
        operations = ['+', '-', '\u00D7', '\u00F7']
        max_n = 10
        min_n = 1

        if self.point <= 10:
            num1 = random.randint(min_n, max_n)
            num2 = random.randint(min_n, max_n)
        elif self.point > 10 and max_n < 99:
            level = self.point // 10
            if level % 2 == 0:
                max_n += 5
            else:
                min_n += 3

            num1 = random.randint(min_n, max_n)
            num2 = random.randint(min_n, max_n)

        if num2 == 0 and '\u00F7' in operations:  # Avoid division by zero
            num2 = random.randint(min_n, max_n)

        operation = random.choice(operations) #สุ่ม operation
        
        if operation == '+':
            self.answer = num1 + num2
        elif operation == '-':
            self.answer = num1 - num2
        elif operation == '\u00D7':
            self.answer = num1 * num2
        elif operation == '\u00F7':
            self.answer = num1 // num2

        if operation == '\u00F7':
            # กำหนดให้ตัวส่วนไม่เกิน 17
            if num2 > 17 and '\u00F7' in operations:
                num2 = random.randint(1, 17)

            # แก้ไขตัวเลขในกรณีที่ operaton เป็นหารแล้วตัวเศษมีค่าน้อยกว่าตัวส่วน
            if num1 <= num2 and '\u00F7' in operations:
                num1 = random.randint(num2, max_n) # ด้วยวิธีการสุ่มใหม่โดยกำหนดให้ขอบล่างมีค่าเท่ากับ num2
            
            # แก้ไขปัญหาหารไม่ลงตัว 
            while num1 % num2 != 0:
                num1 += 1
                # เมื่อหารไม่ลงตัว num1 มีค่าเพิ่มขึ้น 1 แล้วเพิ่มไปเรื่อยๆ จนกว่าจะหารลงตัว
            
            self.answer = num1 // num2

        question = f"{num1} {operation} {num2} = ?"
        
        return self.answer, question
    
    def option(self):
        options = [self.answer, self.answer + random.randint(1, 5), self.answer - random.randint(1, 5), self.answer + random.randint(6, 10)]
        random.shuffle(options)

        return options