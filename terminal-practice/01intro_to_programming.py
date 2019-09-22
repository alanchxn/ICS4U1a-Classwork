# Topics
#     Variables
#         Assignment operator
#         Variables as containers
#     Datatypes
#         Integer
#         Float
#         String
#         Boolean
#     Output
#         f-strings
#         .format()
#     Input
#         Prompting
#         Type conversion

#storing data in variables
# length = 5
# width = 10
# area = length * width
# print(area)

#get data from user
# name = (input("Please enter your name \n"))
# print("Your name is " + name)

#convert input to number
# the_str = "goodbye" #obviously a string
# another_str = "500" #not obviously a string
# #convert string to an integer
# print(int(another_str)+2)
# #convert string to a float
# print(float(another_str)+2)

# #format output text
# name = "Alan"
# age = 17
# # .format method
# format_text = "Hello, {}. You are {} years old.".format(name, age)
# print(format_text)
# # concatenation method
# concat = "Hello, " + name + ". You are " + str(age) + " years old."
# print(concat)

# #calling functions within functions
# def main():
#     say_hello()
#     say_goodbye()
#     alans_code_is_done()
# def say_hello():
#     print("I was told to say hello")
# def say_goodbye():
#     print("I was told to say goodbye")
# def alans_code_is_done():
#     print("Alan's code is done")
# if __name__ == "__main__":
#     main() 