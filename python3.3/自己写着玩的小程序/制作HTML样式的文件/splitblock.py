def getline(file):
    for line in file:
        yield line
    yield '\n'  #鍔犲叆杩欒鏄负浜嗛槻姝㈣鍙栨渶鍚庝竴琛屽悗閫氳繃b=[]璧嬬┖鍊硷紝瀵艰嚧鍙栦笉鍒版渶鍚庝竴琛?
def getblock(file):
    b=[]
    for liner in getline(file):
        if liner.strip():
            b.append(liner[:-1])
        elif b:
            yield ''.join(b).strip()
            b=[]

