from scrapy.selector import Selector

html = """
<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello Protein-Protein Interaction!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose 
            <a href="https://www.ebi.ac.uk/intact/home">IntAct!</a>!
        </p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Enjoy IntAct!</p>
    </div>
  </body>
</html>
"""

sel = Selector(text=html) 
sel.xpath('//p') # Return a SelectorList of Selector objects
# [<Selector query='//p' data='<p class="class-1 class-2">Hello Prot...'>, <Selector query='//p' data='<p id="p2" class="class-2">Choose \n  ...'>, <Selector query='//p' data='<p class="class-2">Enjoy IntAct!</p>'>]

def print_attribute(xpath, html_content):
    sel = Selector(text=html_content) # Set up the selector, which selects the entire html content
    print("You have selected:")
    for i, el in enumerate(sel.xpath(xpath).extract()):
        print("%d) %s" % (i+1, el))

print_attribute('//p[@id="p2"]/a/@href', html)
