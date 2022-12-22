"""
Latest Earthquake Detection Application
MODULARIZATION WITH FUNCTION
MODULARIZATION WITH PACKAGE
"""
import Latest_Earthquake_Detection

if __name__ =='__main__':
    print('Main Application')
    result = Latest_Earthquake_Detection.extraction_data()
    Latest_Earthquake_Detection.show_data(result)

