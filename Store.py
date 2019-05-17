import Classes

#Section is an area of the store a sales assosciate is responsible for
#Each section has a name and what aisles are in that section
section_A = Classes.Section('A',[1,2,3,4,5,6,7,8,9,10])
section_B = Classes.Section('B',[2,4,6,8,10])
section_0 = Classes.Section('none',[])

#Store is currently just a list of sections
#But it seems like it should be an object
store_ct457 = Classes.Store('ct457',[section_0,section_A,section_B])