# Answer for question: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        substring = string[i:k+i]
        print("".join(list(set(substring))))
        
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)