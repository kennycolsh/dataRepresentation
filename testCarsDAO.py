from Databases import carsDAO
#create
latestid = carsDAO.create(('121KK454','Ford','TT',5545, 2))

# find by id
result = carsDAO.findbyid(latestid);
print (result)

#update
carsDAO.update(('121KK454','DD','SS',54545, 2,latestid))
result = carsDAO.findbyid(latestid);
print (result)

# get all
allcars = carsDAO.getall()
for cars in allcars:
    print(cars)

# delete
carsDAO.delete(latestid)