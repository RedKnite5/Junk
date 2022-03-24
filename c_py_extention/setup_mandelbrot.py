from distutils.core import setup, Extension

def main():
    setup(name="mandelbrot_lib",
          version="1.0.0",
          description="Code for calculating the mandelbrot set quickly",
          author="RedKnite",
          author_email="mr.awesome10000@gmail.com",
          ext_modules=[Extension("mandelbrot_lib", ["mandelbrot_lib.c"])])

if __name__ == "__main__":
    main()
