import generate as gen

def main():
    readme = gen.readMeGen()
    readme.create_readme()
    
if __name__ == "__main__":
    main()