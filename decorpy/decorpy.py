from functools import wraps
from timeit import default_timer


def timer(func):
    """Prints the time taken for the give function to execute"""
    @wraps(func)
    def wrapper_time(*args, **kwargs):
        saved_args = locals()
        start = default_timer()
        func(*args, **kwargs)
        end = default_timer()
        print(
            f"The time taken for the function {func.__name__!r} with args {saved_args} is {(end - start):.6f} seconds.")
    return wrapper_time


def debug(func):
    """Prints function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        # formatting args and kwargs
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Now calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"Call with {func.__name__}({signature}) -> returned {value!r}")

        return value
    return wrapper_debug


def check_types(input=None, output=None):
    """Checks input and output types of function call"""
    def check_decorator(func):
        @wraps(func)
        def check_wrapper(*args, **kwargs):
            # grouping parameters
            total_args = args + tuple(kwargs.values())

            if len(input) == len(total_args):
                for i, a in enumerate(total_args):
                    if not isinstance(a, input[i]):
                        raise Exception(
                            f"The type of {a} and input[{i}] are different : {type(a)} and {input[i]}")
            else:
                raise Exception(
                    f"The function expected {len(input)} parameters.")

            # getting result into tuple
            result = func(*args, **kwargs)
            if not isinstance(result, tuple):
                result = (result, )

            if len(result) == len(output):
                for i, v in enumerate(result):
                    if not isinstance(v, output[i]):
                        raise Exception(
                            f"The type of {v} and {output[i]} are different : {type(v)} and {type(output[i])}")
            else:
                raise Exception(
                    f"The function expected {len(output)} return values.")

            return result
        return check_wrapper
    return check_decorator
