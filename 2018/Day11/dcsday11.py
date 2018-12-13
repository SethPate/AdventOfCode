#dan day 11

grid_serial_number = 6303

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

#build summed area table
def calc_sat_value(a):
    for x in range(1,301):
        for y in range(1,301):
            fuel_cell_index_name_2 = "x" + str(x) + "y" + str(y)
            if y > 1:
                fuel_cell_index_name_prev =  "x" + str(x) + "y" + str(y - 1)
                a[fuel_cell_index_name_2].sat_value += a[fuel_cell_index_name_prev].sat_value
    for y in range(1,301):
        for x in range(1,301):
            fuel_cell_index_name_2 = "x" + str(x) + "y" + str(y)
            if x > 1:
                fuel_cell_index_name_prev = "x" + str(x - 1) + "y" + str(y)
                a[fuel_cell_index_name_2].sat_value += a[fuel_cell_index_name_prev].sat_value
    return a

#pad the edges with zero values to prevent null errors.
def add_zeroes(a):
    for x in range(0,301):
        fuel_cell_index['x' + str(x) + 'y0'] = FuelCell(x,0)
        fuel_cell_index['x' + str(x) + 'y0'].sat_value = 0
    for y in range(0,301):
        fuel_cell_index['x0y' + str(y)] = FuelCell(0,y)
        fuel_cell_index['x0y' + str(y)].sat_value = 0
    return a

class FuelCell:
    _registry =[]
    
    def __init__(self,x,y):
        self._registry.append(self)
        self.x_coordinate = x
        self.y_coordinate = y
        self.rack_id = x + 10
        self.power_level = 0
        self.tbt_power = 0
        self.tbt_power_z_calc = 0
        self.tbt_power_z = 0
        self.max_z = 0
        self.sat_value = 0
        self.max_sat_value = 0
        
    def calc_power_level(self):
        self.power_level = (self.rack_id * self.y_coordinate) + grid_serial_number
        self.power_level *= self.rack_id
        pl_string = str(self.power_level)
        pl_len = len(pl_string)
        if pl_len >= 3:
            self.power_level = int(pl_string[-3])
        else:
            self.power_level = 0
        self.power_level += -5
        self.sat_value = self.power_level
        
    def calc_tbt_power(self):
        if self.x_coordinate <= 298 and self.y_coordinate <= 298:
            for m in range(0 + self.x_coordinate,3 + self.x_coordinate):
                for n in range(0 + self.y_coordinate,3 + self.y_coordinate):
                    fuel_cell_index_name_2 = "x" + str(m) + "y" + str(n)
                    self.tbt_power += int(fuel_cell_index[fuel_cell_index_name_2].power_level)
    
    def calc_tbt_power_z(self):
        max_size = min(300 - self.x_coordinate + 1, 300 - self.y_coordinate + 1)
        self.max_z = 1
        test_sat_value = self.power_level
        self.max_sat_value = self.power_level
        for i in range(2,max_size):
            test_sat_value = fuel_cell_index["x" + str(self.x_coordinate - 1 ) + "y" + str(self.y_coordinate - 1)].sat_value
            test_sat_value += fuel_cell_index["x" + str(self.x_coordinate -1 + i ) + "y" + str(self.y_coordinate - 1 + i)].sat_value
            test_sat_value -= fuel_cell_index["x" + str(self.x_coordinate - 1 + i ) + "y" + str(self.y_coordinate - 1)].sat_value
            test_sat_value -= fuel_cell_index["x" + str(self.x_coordinate - 1 ) + "y" + str(self.y_coordinate - 1 + i)].sat_value
            if test_sat_value > self.max_sat_value:
                self.max_sat_value = test_sat_value
                self.max_z = i

#create all of the fuel cells
k = 0

fuel_cell_index = {}
power_index = {}

for i in range(1,301):
    for j in range(1,301):
        fuel_cell_index_name = "x" + str(i) + "y" + str(j)
        fuel_cell_index[fuel_cell_index_name] = FuelCell(i,j)
        fuel_cell_index[fuel_cell_index_name].calc_power_level()

for item in FuelCell._registry:
    fuel_cell_index_name = "x" + str(item.x_coordinate) + "y" + str(item.y_coordinate)
    fuel_cell_index[fuel_cell_index_name].calc_tbt_power()
        
for item in FuelCell._registry:
    fuel_cell_index_name = "x" + str(item.x_coordinate) + "y" + str(item.y_coordinate)
    power_index[fuel_cell_index_name] = int(fuel_cell_index[fuel_cell_index_name].tbt_power)

print("11a: " + str(keywithmaxval(power_index)))

#11b
power_index_z = {}

#using a summed-area table approach.
fuel_cell_index = calc_sat_value(fuel_cell_index)
fuel_cell_index = add_zeroes(fuel_cell_index)

for item in FuelCell._registry:
    if item.x_coordinate > 0 and item.y_coordinate > 0:
        fuel_cell_index_name = "x" + str(item.x_coordinate) + "y" + str(item.y_coordinate)
        fuel_cell_index[fuel_cell_index_name].calc_tbt_power_z()
        power_index_z[fuel_cell_index_name] = int(fuel_cell_index[fuel_cell_index_name].max_sat_value)

max_key = keywithmaxval(power_index_z)

print("11b: " + max_key + "z" + str(fuel_cell_index[max_key].max_z))
