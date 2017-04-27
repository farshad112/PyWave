import re
import time

class PyColor:
    default_color="White"
    default_response_mode = "default_color"
    name =""      #
    rgb_hex_string=""   # RGB hex string for corresponding color code
    rgb_hex_tuple=[]    # RGB hex tuple for corresponding color code
    rgba_hex_tuple=[]   # RGBA hex tuple for corresponding color code
    
    colors = {
        'AliceBlue ': '#F0F8FF',
        'AntiqueWhite': '#FAEBD7',
        'Aqua': '#00FFFF',
        'Aquamarine': '#7FFFD4',
        'Azure': '#F0FFFF',
        'Beige': '#F5F5DC',
        'Bisque': '#FFE4C4',
        'Black': '#000000',
        'BlanchedAlmond': '#FFEBCD',
        'Blue': '#0000FF',
        'BlueViolet': '#8A2BE2',
        'Brown': '#A52A2A',
        'BurlyWood': '#DEB887',
        'CadetBlue': '#5F9EA0',
        'Chartreuse': '#7FFF00',
        'Chocolate': '#D2691E',
        'Coral': '#FF7F50',
        'CornflowerBlue': '#6495ED',
        'Cornsilk': '#FFF8DC',
        'Crimson': '#DC143C',
        'Cyan': '#00FFFF',
        'DarkBlue': '#00008B',
        'DarkCyan': '#008B8B',
        'DarkGoldenRod': '#B8860B',
        'DarkGray': '#A9A9A9',
        'DarkGreen': '#006400',
        'DarkKhaki': '#BDB76B',
        'DarkMagenta': '#8B008B',
        'DarkOliveGreen': '#556B2F',
        'DarkOrange': '#FF8C00',
        'DarkOrchid': '#9932CC',
        'DarkRed': '#8B0000',
        'DarkSalmon': '#E9967A',
        'DarkSeaGreen': '#8FBC8F',
        'DarkSlateBlue': '#483D8B',
        'DarkSlateGray': '#2F4F4F',
        'DarkTurquoise': '#00CED1',
        'DarkViolet': '#9400D3',
        'DeepPink': '#FF1493',
        'DeepSkyBlue': '#00BFFF',
        'DimGray': '#696969',
        'DodgerBlue': '#1E90FF',
        'FireBrick': '#B22222',
        'FloralWhite': '#FFFAF0',
        'ForestGreen': '#228B22',
        'Fuchsia': '#FF00FF',
        'Gainsboro': '#DCDCDC',
        'GhostWhite': '#F8F8FF',
        'Gold': '#FFD700',
        'GoldenRod': '#DAA520',
        'Gray': '#808080',
        'Green': '#008000',
        'GreenYellow': '#ADFF2F',
        'HoneyDew': '#F0FFF0',
        'HotPink': '#FF69B4',
        'Indian red': '#B0171F',
        'Indigo': '#4B0082',
        'Ivory': '#FFFFF0',
        'Khaki': '#F0E68C',
        'Lavender': '#E6E6FA',
        'LavenderBlush': '#FFF0F5',
        'LawnGreen': '#7CFC00',
        'LemonChiffon': '#FFFACD',
        'LightBlue': '#ADD8E6',
        'LightCoral': '#F08080',
        'LightCyan': '#E0FFFF',
        'LightGoldenRodYellow': '#FAFAD2',
        'LightGray': '#D3D3D3',
        'LightGreen': '#90EE90',
        'Lightpink': '#FFB6C1',
        'LightSalmon': '#FFA07A',
        'LightSeaGreen': '#20B2AA',
        'LightSkyBlue': '#87CEFA',
        'LightSlateGray': '#778899',
        'LightSteelBlue': '#B0C4DE',
        'LightYellow': '#FFFFE0',
        'Lime': '#00FF00',
        'LimeGreen': '#32CD32',
        'Linen': '#FAF0E6',
        'Magenta': '#FF00FF',
        'Maroon': '#800000',
        'MediumAquaMarine': '#66CDAA',
        'MediumBlue': '#0000CD',
        'MediumOrchid': '#BA55D3',
        'MediumPurple': '#9370DB',
        'MediumSeaGreen': '#3CB371',
        'MediumSlateBlue': '#7B68EE',
        'MediumSpringGreen': '#00FA9A',
        'MediumTurquoise': '#48D1CC',
        'MediumVioletRed': '#C71585',
        'MidnightBlue': '#191970',
        'MintCream': '#F5FFFA',
        'MistyRose': '#FFE4E1',
        'Moccasin': '#FFE4B5',
        'NavajoWhite': '#FFDEAD',
        'Navy': '#000080',
        'OldLace': '#FDF5E6',
        'Olive': '#808000',
        'OliveDrab': '#6B8E23',
        'Orange': '#FFA500',
        'OrangeRed': '#FF4500',
        'Orchid': '#DA70D6',
        'PaleGoldenRod': '#EEE8AA',
        'PaleTurquoise': '#AFEEEE',
        'PaleVioletRed': '#DB7093',
        'PapayaWhip': '#FFEFD5',
        'PeachPuff': '#FFDAB9',
        'Peru': '#CD853F',
        'Pink': '#FFC0CB',
        'Plum': '#DDA0DD',
        'PowderBlue': '#B0E0E6',
        'Purple': '#800080',
        'RebeccaPurple': '#663399',
        'Red': '#FF0000',
        'RosyBrown': '#BC8F8F',
        'RoyalBlue': '#4169E1',
        'SaddleBrown': '#8B4513',
        'Salmon': '#FA8072',
        'SandyBrown': '#F4A460',
        'SeaGreen': '#2E8B57',
        'SeaShell': '#FFF5EE',
        'Sienna': '#A0522D',
        'Silver': '#C0C0C0',
        'SkyBlue': '#87CEEB',
        'SlateBlue': '#6A5ACD',
        'SlateGray': '#708090',
        'Snow': '#FFFAFA',
        'SpringGreen': '#00FF7F',
        'SteelBlue': '#4682B4',
        'Tan': '#D2B48C',
        'Teal': '#008080',
        'Thistle': '#D8BFD8',
        'Tomato': '#FF6347',
        'Turquoise': '#40E0D0',
        'Violet': '#EE82EE',
        'Wheat': '#F5DEB3',
        'White': '#FFFFFF',
        'WhiteSmoke': '#F5F5F5',
        'Yellow': '#FFFF00',
        'YellowGreen': '#9ACD32'}
    
    def __init__(self, color_name='White', transparency=0.0, default_response_mode='default_color'):
        '''
        constructor for creating a color.
        :param color_name: String containing the color name in English
        :param transparency: float ranging from 0.0 to 1.0
        :param default_response_mode: how to behave when a color is not found. default is 'default_color'
        '''
        self.update_color(color_name, transparency)
        self.set_default_response_mode(default_response_mode)
        
    def resolve_color_name(self, color_name):
        '''
        Searches for the color name within the colors dictionary. If specified color name matches with the dictionary 'key' then returns the key
        :param color_name: String for specifying color name
        :return: dictionary key as string if color is found within the dictionary key otherwise returns 'colorNotFound'
        '''
        for i in self.colors:
            if i.lower() == color_name.lower():
                self.name = i
                return i
        return "colorNotFound"
    
    def update_color(self, color_name, transparency_val = 0.0):
        '''
        Updates all color attributes (RGB Hex string, rgb Hex tuple, RGBA hex tuple) for the specified color name.
        :param color_name: String for specifying color name
        :param transparency_val: float ranging from 0.0 to 1.0
        :return: None
        '''
        self.name = color_name
        self.get_rgb_hex_string(color_name)
        self.get_rgb_hex_tuple(color_name)
        self.get_rgba_hex_tuple(color_name, transparency_val)
    
    def get_default_response(self):
        '''
        returns default value when the specified color is not found in the dictionary
        :return: default color value when default_response_mode == 'default_color' otherwise returns 'colorNotFound'
        '''
        if self.default_response_mode == 'default_color':
            return self.default_color
        else:
            return 'colorNotFound'
    
    def set_default_response_mode(self, response_mode):
        '''
        Sets the default_response_mode which will be used to determine what action to take when specified color is not present in the dictionary
        :param response_mode: String representing default action mode. default value 'default_color'
        :return: none
        '''
        self.default_response_mode = response_mode
    
    def get_rgb_hex_string(self, color_name):
        '''
        Returns the RGB hex string representing the specified color
        :param color_name: string containing the specified color name
        :return: RGB hex string for the corresponding color if the color is present in the dictionary otherwise returns default response
        '''
        # returns RGB hex string is color is found. Returns default response if color is not found within dictionary
        self.rgb_hex_string = self.colors.get(self.resolve_color_name(color_name), self.get_default_response())
        return self.rgb_hex_string
    
    def get_rgb_hex_tuple(self, color_name):
        '''
        Returns the RGB hex tuple representing the specified color
        :param color_name: string containing the specified color name
        :return: RGB hex tuple for the corresponding color if the color is present in the dictionary otherwise returns default response
        '''
        # returns RGB hex string is color is found. Returns default response if color is not found within dictionary
        self.rgb_hex_string = self.colors.get(self.resolve_color_name(color_name), self.get_default_response())
        if self.rgb_hex_string != 'colorNotFound':
            # convert string to hexadecimal value
            red_val = self.rgb_hex_string[1:3]
            green_val = self.rgb_hex_string[3:5]
            blue_val = self.rgb_hex_string[5:7]
            self.rgb_hex_tuple = tuple((int(red_val,16),int(green_val,16),int(blue_val,16)))
            return self.rgb_hex_tuple
        else:
            return 'colorNotFound'
    
    def get_rgba_hex_tuple(self, color_name, transparency_val):
        '''
        Returns the RGBA hex tuple representing the specified color and transparency value
        :param color_name: string containing the specified color name
        :param transparency_val: float ranging from 0.0 to 1.0
        :return: RGBA hex tuple for the corresponding color and transparency value if the color is present in the dictionary otherwise returns default response
        '''
        # returns RGB hex string is color is found. Returns default response if color is not found within dictionary
        self.rgb_hex_string = self.colors.get(self.resolve_color_name(color_name), self.get_default_response())
        if self.rgb_hex_string != 'colorNotFound':
            # convert string to hexadecimal value
            red_val = self.rgb_hex_string[1:3]
            green_val = self.rgb_hex_string[3:5]
            blue_val = self.rgb_hex_string[5:7]
            self.rgb_hex_tuple = tuple((int(red_val, 16), int(green_val, 16), int(blue_val, 16)))
            self.rgba_hex_tuple = tuple((int(red_val, 16), int(green_val, 16), int(blue_val, 16),transparency_val))
            return self.rgba_hex_tuple
        else:
            return 'colorNotFound'
    
    def list_available_colors(self):
        '''
        Print Name of All Available Color in the dictionary
        :return: none
        '''
        for i in self.colors:
            print(i)
            
    def update_color_by_string(self, hexcode):
        '''
        Updates all color attributes (RGB string, RGB tuple , RGBA tuple) for user defined RGB hexcolor string
        :param hexcode: String containing RGB hex code for user defined color
        :return: none
        '''
        self.rgb_hex_string = hexcode
        # convert string to hexadecimal value
        red_val = self.rgb_hex_string[1:3]
        green_val = self.rgb_hex_string[3:5]
        blue_val = self.rgb_hex_string[5:7]
        # update the RGB tuples
        self.rgb_hex_tuple = tuple((int(red_val, 16), int(green_val, 16), int(blue_val, 16)))
        self.rgba_hex_tuple = tuple((int(red_val, 16), int(green_val, 16), int(blue_val, 16), 0.0))
    
    def update_color_by_rgb_tuple(self, hexcode):
        '''
        Updates all color attributes (RGB string, RGB tuple , RGBA tuple) for user defined RGB hexcolor tuple
        :param hexcode: Tuple containing RGB hex code for user defined color
        :return: none
        '''
        self.rgb_hex_tuple = hexcode
        self.rgba_hex_tuple = tuple((hexcode,0.0))
        # convert the tuple into equivalent RGB string
        self.rgb_hex_string = '#' + ''.join(map(chr,hexcode)).encode('hex')
        
    def update_color_by_rgba_tuple(self, hexcode):
        '''
        Updates all color attributes (RGB string, RGB tuple , RGBA tuple) for user defined RGBA hexcolor tuple
        :param hexcode: Tuple containing RGBA hex code for user defined color
        :return: none
        '''
        self.rgba_hex_tuple = hexcode
        self.rgb_hex_tuple = tuple(hexcode[0:4])
        # convert the tuple into equivalent RGB string
        self.rgb_hex_string = '#' + ''.join(map(chr, self.rgb_hex_tuple)).encode('hex')
    
    def set_color_by_code(self, hexcode, color_name=""):
        '''
        Updates all color attributes (RGB string, RGB tuple , RGBA tuple) for user defined code (i.e. String/Tuple)
        :param hexcode: Can be a RGB string, RGB tuple or RGBA tuple
        :param color_name: String for defining user defined color
        :return: none
        '''
        self.name = color_name
        if isinstance(hexcode, str):
            # Check for valid hex code
            hex_pattern = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
            if hex_pattern.match(hexcode):
                self.update_color_by_string(hexcode)
            else:
                print("RGB CODE ERROR :: Not a valid RGB color code")
                time.sleep(5) # delay for 5 second
                exit() # terminate the script
        elif isinstance(hexcode,tuple):
            if len(hexcode) == 3: # parameter type RGB tuple
                # check for valid color values in tuple
                for i in hexcode:
                    if i < 0 and i >256:
                        print(str(i) +"is not a valid RGB tuple value")
                        time.sleep(5) # delay for 5 second
                        exit() # terminate the script
                self.update_color_by_rgb_tuple(hexcode)
            elif len(hexcode) == 4: # parameter type rgba tuple
                # check for valid color value in tuple
                for i, j in enumerate(hexcode):
                    if i < 4 and j < 0 and j > 255:
                        print(str(j) + "is not a valid RGB tuple value")
                        time.sleep(5)  # delay for 5 second
                        exit()  # terminate the script
                    elif i == 4 and j < 0 and j > 1:
                        print(str(j) + "is not a valid transparency value")
                        time.sleep(5)  # delay for 5 second
                        exit()  # terminate the script
                self.update_color_by_rgba_tuple(hexcode)
            else:
                print(hexcode + "is not a valid RGB tuple value")
                time.sleep(5)  # delay for 5 second
                exit()  # terminate the script
        else:
            print("Input is not in valid color format. \nPlease use either srting as RGB hexcode i.e. #FF00FF or RGB tuple i.e. (255,0,255) or RGBA tuple i.e. (255,0,255,0.5)")
            time.sleep(5)  # delay for 5 second
            exit()  # terminate the script
     
    def set_color_name(self, color_name):
        '''
        set the color name
        :param color_name: String containing the color name
        :return: none
        '''
        self.name = color_name
        
# if __name__ == "__main__":
#     color = PyColor("Yellow")
#     print("Printing Attributes of Color :: Yellow")
#     print(color.rgba_hex_tuple)
#     print(color.rgb_hex_tuple)
#     print(color.rgb_hex_string)
#     color2 = PyColor("RED")
#     print("Printing Attributes of Color :: RED")
#     print(color2.rgba_hex_tuple)
#     print(color2.rgb_hex_tuple)
#     print(color2.rgb_hex_string)
