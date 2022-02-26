class Solution:
       
    
    def numberToWords(self,num):  

        mappers = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        result = ""
        if num in mappers:
            if str(num)[0] == '1' and num%10 == 0 and num>10:
                return "One " + mappers[num]

            return mappers[num]
        
        elif num < 100:
            result = mappers[(num//10)*10] + " " + mappers[num%10]
        
        else:
            size = len(str(num))
            cof = (size-size%3)
           
            if size == 3:
                last_part = self.numberToWords(num%100) if self.numberToWords(num%100) != 'Zero' else ""
                result = mappers[(num//100)] + " " + mappers[100] + " " + last_part 
            
            else:
                if size%3 == 0:
                    last_part =  self.numberToWords(num%10**(size-3)) if  self.numberToWords(num%10**(size-3)) != 'Zero' else ""
                    result += self.numberToWords(num//10**(size-3)) + " " + mappers[10**(size-3)] + " " + last_part
                else:
                    last_part =  self.numberToWords(num%10**cof) if  self.numberToWords(num%10**cof) != 'Zero' else ""
                    result =  self.numberToWords(num//10**cof) + " " + mappers[10**cof] + " " + last_part

        return result.strip()


sol = Solution()

print(sol.numberToWords(25942))
