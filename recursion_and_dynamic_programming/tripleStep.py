def tripleStep(steps: int) -> int:
    if steps < 0:
        return 0 
    if steps == 0:
        return 1
    else:
        return tripleStep(steps-1) + tripleStep(steps-2) + tripleStep(steps-3)


if __name__ == "__main__":
    print(tripleStep(2))