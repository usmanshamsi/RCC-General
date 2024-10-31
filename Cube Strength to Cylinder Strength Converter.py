# input value of cube strength
cube_strength = 4000       #psi


# data table
cube_strengths = (1300.0, 2200.0, 2900.0, 3600.0, 4000.0, 4200.0, 4300.0, 5200.0, 5300.0, 6100.0, 6400.0,7000.0, 7600.0)
# factor = cylinder / cube
factors = (.77, .77, .76, .81, .87, .91, .91, .89, .94, .87, .92, .91, .96)
cylinder_strengths = (1000.0, 1700.0, 2200.0, 2900.0, 3500.0, 3800.0, 3900.0, 4600.0, 5000.0, 5300.0, 5900.0, 6400.0, 7300.0)
CONVERSION_DATA_LENGTH = len(cube_strengths)

# definition of cube to cylinder function
def cubeToCylinder(cubeStrength):
    # conversion factor
    factor = 1

    # Extreme Lower Limit check
    if (cubeStrength <= cube_strengths[0]):
        factor = factors[0]
    # extreme upper limit check
    elif (cubeStrength >= cube_strengths[CONVERSION_DATA_LENGTH-1]):
        factor = factors[CONVERSION_DATA_LENGTH-1]
    # intermediate values check
    else:
        for i in range(0,CONVERSION_DATA_LENGTH-1):
            if (cubeStrength == cube_strengths[i]):
                factor = factors[i]
            elif (cubeStrength == cube_strengths[i+1]):
                factor = factors[i+1]
            elif (cubeStrength > cube_strengths[i] and cubeStrength < cube_strengths[i+1]):
                factor = factors[i] + (factors[i+1]-factors[i])/(cube_strengths[i+1]-cube_strengths[i])*(cubeStrength-cube_strengths[i])

    cylinderStrength = cubeStrength * factor

    return factor, cylinderStrength

def main():
    import os
    os.system('cls')
    result = cubeToCylinder(cube_strength)
    print(f"Conversion factor = {result[0]} ")
    print(f"Cylinder strength = {result[1]} psi")
    print()

if __name__ == "__main__":
    main()
