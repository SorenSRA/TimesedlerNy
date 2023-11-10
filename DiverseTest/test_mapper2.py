# Import af egne pakker
import sys
import os


def main():
    pr = "test"
    match pr:
        case "test":
            project = c.Test()
        case _:
            project = c.Bet()

    print(project.rootpath)
    print(project.sourcepath)
    print(project.filspec)
    print(project.filpath)
    print(project.destinationpath)


if __name__ == "__main__":
    print(sys.path)
    akt_dir = os.path.dirname(os.path.abspath(__file__))
    cons_dir = r"..\constants"
    sys.path.append(os.path.join(akt_dir, cons_dir))
    print(sys.path)
    import constants as c

    main()
