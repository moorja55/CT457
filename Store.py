import Classes

#Section is an area of the store a sales assosciate is responsible for
#Each section has a name and what aisles are in that section
section_0 = Classes.Section('none',[[0,0]])
section_1 = Classes.Section('Sports/Auto',[[1,35]])
section_2 = Classes.Section('Home/Seasonal',[[44,84],[97,111]])
section_3 = Classes.Section('Seasonal/Decor',[[64,84],[97,111]])
section_4 = Classes.Section('Sports',[[21,22],[26,43]])
section_5 = Classes.Section('Auto',[[1,20],[23,25]])
section_6 = Classes.Section('Home Improvement',[[44,84]])
section_7 = Classes.Section('Seasonal',[[97,111]])
section_8 = Classes.Section('Kitchen Place',[[75,84]])
section_9 = Classes.Section('Parts Desk',[[9,14]])
section_10 = Classes.Section('Kid Zone',[[31,35]])
section_11 = Classes.Section('Paint and Tools',[[44,54]])
section_12 = Classes.Section('Patio / BBQ',[[97,101]])
section_Z = Classes.Section('facing',[[0,0]])

#Store is currently just a list of sections
#But it seems like it should be an object
store_ct457 = Classes.Store('ct457',[section_0,section_1,section_2,section_3,section_4,section_5,section_6,section_7,section_8,section_9,section_10,section_11,section_12,section_Z])