import matplotlib.pyplot as plt
import numpy


class Car:
    name = ""
    body = ""
    wheelbase  = 0
  #trackwidth = 0
    frontwidth = 0
    backwidth = 0

    def __init__(self, name, body, wheelbase, frontwidth, backwidth):
        self.name = name
        self.body = body
        self.wheelbase = wheelbase
        self.frontwidth = frontwidth
        self.backwidth = backwidth


def main():
    carlist = []
    
    #Sedan
    carlist.append(Car("Maruti Suzuki Dzire", "Sedan", 2450, 1530, 1520))
    carlist.append(Car("Maruti Suzuki Ciaz", "Sedan", 2650, 1495, 1505))
    carlist.append(Car("Tata Tigor", "Sedan", 2450, 1400, 1420))
    carlist.append(Car("Hyundai Verna (Old)","Sedan",  2570, 1495, 1502))
    carlist.append(Car("BMW 7 Series", "Sedan", 3210, 1611, 1650))
    carlist.append(Car("Jaguar XJ", "Sedan",3157 , 1626, 1604))
    carlist.append(Car("Skoda Rapid", "Sedan",2552 ,1457 ,1500 ))
    carlist.append(Car("Hyundai Xcent", "Sedan", 2425, 1479, 1493))
    carlist.append(Car("Hyundai Elantra", "Sedan", 2700, 1555, 1564))
    carlist.append(Car("BMW 3 Series", "Sedan", 2810, 1544, 1583))
    
    #Hatchback
    carlist.append(Car("Renault Kwid", "Hatchback", 2422, 1387, 1382))
    carlist.append(Car("Maruti suzuki Wagon R","Hatchback",2435 ,1295 , 1290))
    carlist.append(Car("Maruti Suzuki Swift (New)","Hatchback",2450 , 1520,1520 ))
    carlist.append(Car("Maruti Suzuki Alto 800","Hatchback", 2360, 1295,1290 ))
    carlist.append(Car("Tata Tiago", "Hatchback",2400, 1400, 1420))
    carlist.append(Car("Maruti Suzuki Baleno","Hatchback",2520 ,1515 , 1525))
    carlist.append(Car("Hyundai i20", "Hatchback",2570,1505 , 1503))
    carlist.append(Car("Hyundai Grand i10", "Hatchback",2425, 1479 , 1493))
    carlist.append(Car("Hyundai Santro", "Hatchback",2400, 1463, 1481))
    carlist.append(Car("Volkswagen Polo", "Hatchback",2469, 1460,1456 ))

    #SUV
    carlist.append(Car("Mahindra Scorpio", "SUV", 2680,1450 ,1450 ))
    carlist.append(Car("Mahindra Thar", "SUV",2430, 1445,1346 ))
    carlist.append(Car("Renault Duster", "SUV",2673,1560 ,1567 ))
    carlist.append(Car("Toyota Fortuner", "SUV",2750, 1540, 1540))
    carlist.append(Car("Mahindra Bolero", "SUV",2680, 1472,1462 ))
    carlist.append(Car("Maruti Suzuki Vitara Brezza", "SUV", 2500, 1535, 1505))
    carlist.append(Car("Toyota Land Cruiser", "SUV", 2850, 1640, 1635))
    carlist.append(Car("Mercedes-AMG G 63", "SUV", 2850, 1475, 1475))
    carlist.append(Car("KUV100 NXT", "SUV", 2385, 1490, 1490))
    carlist.append(Car("Ford Endeavour", "SUV", 2850, 1560, 1564))
    

    body_to_color = {"Sedan": "#e41a1c", "Hatchback": "#377eb8", "SUV": "#4daf4a"}
    
    x = []
    y = []
    z = []
    
    for i in range(len(carlist)):
        x.append(carlist[i].wheelbase)
        y.append(carlist[i].frontwidth)
        z.append(body_to_color[carlist[i].body])

    sedan = [ (car.wheelbase,car.frontwidth) for car in carlist if car.body == "Sedan"]
    hatchback = [ (car.wheelbase,car.frontwidth) for car in carlist if car.body == "Hatchback"]
    suv = [ (car.wheelbase,car.frontwidth) for car in carlist if car.body == "SUV"]
    
    x, y = zip(* sedan)
    plt.scatter(x, y, s = None, color=body_to_color["Sedan"], label="Sedan")
    x, y = zip(* hatchback)
    plt.scatter(x, y, s = None, color=body_to_color["Hatchback"], label="Hatchback")
    x, y = zip(* suv)
    plt.scatter(x, y, s = None, color=body_to_color["SUV"], label="SUV")

    x, y = zip(* (sedan + hatchback + suv))
    coeffs = numpy.polyfit(x, y, 2) #2nd degree polynomial fit
    x2 = numpy.arange(min(x) - 1, max(x) + 1, 0.01)
    y2 = numpy.polyval(coeffs, x2)

    plt.plot(x2, y2, '--', color='black', label="2nd deg polynomial fit")

    leg = plt.legend(loc='lower right', frameon=True)
    plt.show()


main()
