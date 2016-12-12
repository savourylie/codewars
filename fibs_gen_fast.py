def fibonacci(n):
    fibs = {0: 0, 1: 1}
    def fibs_gen(n):
        yield fibs[0]
        yield fibs[1]

        while len(fibs) < n + 1:
            fibs[len(fibs)] = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]
            yield fibs[len(fibs) - 1]
            
    result = fibs_gen(n)
    
    for i in range(n):
        result.next()

    return result.next()