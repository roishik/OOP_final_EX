import numpy as np
import cv2 as cv


def main():
    img = np.random.rand(600, 900, 3)
    params = [img, (200, 200), 63, (0, 255, 0)]
    cv.circle(*params, 10)
    cv.circle(img, (200, 200), 63, (255, 0, 0), -1)


    cv.imshow('RGB', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
