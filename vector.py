import math


class PyVector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PyVector2D: (x: {self.x}, y: {self.y})"

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False

    def __le__(self, other):
        if self.x <= other.x and self.y <= other.y:
            return True
        return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self.x != other.x and self.y != other.y:
            return True
        return False

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        return False

    def __ge__(self, other):
        if self.x >= other.x and self.y >= other.y:
            return True
        return False

    # Arithmetic
    def __add__(self, other):
        return PyVector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return PyVector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return PyVector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return PyVector2D(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return PyVector2D(self.x // other.x, self.y // other.y)

    def __abs__(self):
        return PyVector2D(abs(self.x), abs(self.y))

    def __round__(self, n=None):
        return PyVector2D(round(self.x, n), round(self.y, n))

    # Methods
    def clamp_axes(self, min_value: float, max_value: float):
        x = max(min(self.x, float(max_value)), float(min_value))
        y = max(min(self.y, float(max_value)), float(min_value))
        return PyVector2D(x, y)

    def components_equal(self) -> bool:
        """
        Checks whether the components of the vector are equal.
        :return: Bool
        """
        if self.x == self.y:
            return True
        return False

    def components_nearly_equal(self, tolerance) -> bool:
        """
        Checks whether the components of the vector are nearly equaly within a tolerance.
        :param tolerance: The acceptable tolerance.
        :return: Bool
        """
        if (tolerance * -1) <= self.x - self.y <= tolerance:
            return True
        return False

    def component_max(self) -> float:
        """
        Returns the component of the highest value.
        :return: Float
        """
        if self.x > self.y:
            return self.x
        return self.y

    def component_min(self) -> float:
        """
        Returns the component of the lowest value.
        :return: Float
        """
        if self.x < self.y:
            return self.x
        return self.y

    def contains_nan(self):
        """
        Checks whether either component is NaN
        :return: Bool
        """
        if math.isnan(self.x) or math.isnan(self.y):
            return True
        return False

    def cross_product(self, other) -> float:
        """
        Calculate the cross product of two vectors.
        :param other: Other vector
        :return: Float
        """
        return (self.x * other.y) - (self.y * other.x)

    def distance(self, other) -> float:
        """
        Distance between two 2D points.
        :param other: Other Vector
        :return: Float
        """
        x = other.x - self.x
        y = other.y - self.y
        return math.sqrt((x**2 + y**2))

    def distance_squared(self, other) -> float:
        """
        Squared distance between two 2D points.
        :param other: Other Vector
        :return: Float
        """
        x = other.x - self.x
        y = other.y - self.y
        return x**2 + y**2

    def equals(self, other, tolerance=0.0) -> bool:
        """
        Checks for equality with error-tolerant comparison.
        :param other: Other Vector
        :param tolerance: Tolerance of the nearly equal.
        :return:
        """
        if (tolerance * -1) <= self.x - other.x <= tolerance and (tolerance * -1) <= self.y - other.y <= tolerance:
            return True
        return False

    def get_rotated(self, angle_deg):
        """
        Rotates around axis (0,0,1)
        :param angle_deg: Angle to rotate (in degrees)
        :return: Rotated Vector
        """
        cos_x = self.x * math.cos(angle_deg) - self.y * math.sin(angle_deg)
        cos_y = self.x * math.sin(angle_deg) + self.y * math.cos(angle_deg)
        return PyVector2D(cos_x, cos_y)

    def is_nearly_zero(self, tolerance) -> bool:
        """
        Checks whether vector is near to zero within a specified tolerance.
        :param tolerance: Error tolerance.
        :return: true if vector is in tolerance to zero, otherwise false.
        """
        if (tolerance * -1) <= self.x - self.y <= tolerance:
            return True
        return False

    def is_zero(self) -> bool:
        """
        Checks whether all components of the vector are exactly zero.
        :return: true if vector is exactly zero, otherwise false.
        """
        if self.x == 0.0 and self.y == 0.0:
            return True
        return False

    def max(self, other):
        """
        Returns a vector with the maximum component for each dimension from the pair of vectors.
        :param other: Other Vector
        :return: The max vector.
        """
        rtnvect = PyVector2D()
        if self.x > other.x:
            rtnvect.x = self.x
        else:
            rtnvect.x = other.x
        if self.y > other.y:
            rtnvect.y = self.y
        else:
            rtnvect.y = other.y
        return rtnvect

    def min(self, other):
        """
        Returns a vector with the minimum component for each dimension from the pair of vectors.
        :param other: Other Vector
        :return: The min vector.
        """
        rtnvect = PyVector2D()
        if self.x < other.x:
            rtnvect.x = self.x
        else:
            rtnvect.x = other.x
        if self.y < other.y:
            rtnvect.y = self.y
        else:
            rtnvect.y = other.y
        return rtnvect

    def normalize(self, tolerance=0.0):
        """
        Normalize this vector in-place if it is large enough, set it to (0,0) otherwise.
        :param tolerance: Minimum squared length of vector for normalization.
        """
        magnitude = math.sqrt(self.x**2 + self.y**2)
        if (tolerance * -1) <= self.x / magnitude <= tolerance and (tolerance * -1) <= self.y / magnitude <= tolerance:
            self.x = self.x / magnitude
            self.y = self.y / magnitude
        else:
            self.x = 0.0
            self.y = 0.0

    def set(self, in_x, in_y):
        """
        Set the values of the vector directly.
        :param in_x: New X coordinate.
        :param in_y: New Y coordinate.
        """
        self.x = in_x
        self.y = in_y

    def size(self) -> float:
        """
        Get the length (magnitude) of this vector.
        :return: The length of this vector.
        """
        return math.sqrt(self.x**2 + self.y**2)

    def size_squared(self) -> float:
        """
        Get the squared length of this vector.
        :return: The squared length of this vector.
        """
        magnitude = math.sqrt(self.x**2 + self.y**2)
        return magnitude * magnitude













#TODO Vector3D, Vector4D - AllComponentsEqual