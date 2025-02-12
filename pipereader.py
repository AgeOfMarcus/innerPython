'''
Take data piped in and output result of running it through a reader function.
'''

import sys, base64 

def reader_b64(data): # reader that base64 encodes data
    return base64.b64encode(data)

def main(reader=reader_b64): # the main program
    data = sys.stdin.buffer.read() # get raw input
    res = reader(data) # do the thingy
    sys.stdout.buffer.write(res) # print raw bytes 
main() if __name__ == "__main__" else None