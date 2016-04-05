# Range Expansion Image Analysis in Fiji

Preprocessing routines for the python based ["Range Expansion Analysis"](https://github.com/btweinstein/range-expansion-analysis) 
program.

I personally find that programming user input in Python is quite difficult. 
In contrast, user input is extremely easy to accept in [Fiji](http://fiji.sc/). 
Consequently, for our imperfect biological data, I use Fiji to preprocess 
the images and create binary masks. The masks are then analyzed in the [Range Expansion](https://github.com/btweinstein/range-expansion-analysis) 
Python package.

## Installation
Clone this git repository into the "plugins" folder of your [Fiji](http://fiji.sc/) installation. So, just use

```bash
cd PATH/TO/FIJI/plugins/
git clone https://github.com/btweinstein/range_expansion_analysis_fiji.git
```

## Usage

0. Extract all images using the bioformats plugin to a folder called
"tif"
