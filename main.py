import numpy as np
import cv2 as cv


def main():
    img = np.random.rand(600, 900, 3)
    cv.imshow('RGB', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
