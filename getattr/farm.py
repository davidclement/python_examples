import re

class Farm:

    '''
    The purpose of this Farm class is to demonstrate how 
    to use a naming convention for methods so that the 
    methods can be found using their names by constructing
    string objects that are == to their names

    so instead of 
    if crop == 'plumbs':
        self._grow_plumbs()

    ...and repeating that for each crop, we have just one
    "grow" method that finds the right _grow_ method by
    constructing it's name based on the convention...

    ===========
    example
    ===========
    >>> import farm
    >>> f = farm.Farm()
    >>> f.totals
    bananas: 0
    plumbs: 0
    strawberries: 0
    >>> f.grow('strawberries')
    bananas: 0
    plumbs: 0
    strawberries: 200
    >>> f.grow('strawberries')
    bananas: 0
    plumbs: 0
    strawberries: 400
    >>> f.grow('bananas')
    bananas: 100
    plumbs: 0
    strawberries: 400
    >>> f.grow('carrots')
    I don't know how to grow carrots
    bananas: 100
    plumbs: 0
    strawberries: 400
    '''
	
    def _grow_bananas(self):
        self.bananas = getattr(self,'bananas',0) + 100

    def _grow_strawberries(self):
        self.strawberries = getattr(self,'strawberries',0) + 200

    def _grow_plumbs(self):
        self.plumbs = getattr(self,'plumbs',0) + 400

    def grow(self,crop):
        method = getattr(self,'_grow_%s' % crop, None)
        if method:
            method()
        else:
            print "I don't know how to grow {}".format(crop)
        self.totals

    @property
    def totals(self):
        crops = [re.search(r'^_grow_(.*)$',x).group(1) for x in dir(self) if x.startswith('_grow_')]
        output = []
        for c in crops:
            amount = getattr(self,c,0)
            output.append("{}: {}".format(c,amount))
            print "{}: {}".format(c,amount)

        #return "\n".join(output)





