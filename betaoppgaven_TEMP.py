class Oppgave_1:
    def __init__(self) -> None:
        '''
        100% EK finansiert
        '''    
        self.ErE = 0.14 # [forventet avkastning på egenkapitalen]
        self.Rf = 0.02 
        self.ErM = 0.08 #[forventet avkastning på markedsportoføljen] 
        self.mer_info()

    
        '''
        Bi: inversteringsBeta 
        Be: EgenkapitalsBeta
        Bg: gjeldsBeta 
        Bu: beta for selskap uten gjeld
        Bi = Bu 
        ErI = estimert avkastnings for investeringen

        wE & wG : står for vekt / weight som betyr hvor mye av kapitalen er gjeld (wG) i % og hvor mye av kapitalen er EK (wE) i %

        Be = Bu + (G/E)*(Bu-Bg)
        

        Bi = (Be * wE) + (Bg * wG)

        Bi = (ErI - Rf) /(ErM - Rf)    

        Bi = (cov(rI, rM)) / (var(rM))
        '''


    @property
    def Be(self):
        self.Ke = self.ErE
        '''self.Be  = (self.Ke-self.Rf)/(self.ErM - self.Rf)'''
        return (self.Ke-self.Rf)/(self.ErM - self.Rf)
    
    
    def a(self): 
        '''finn Be:'''
        return self.Be

    
    def b(self):
        ''' finn Bi '''
        self.Bu = self.Be #fordi 100% EK finansiert er Be = Bu 

        '''self.Bi = (self.Be * self.wE) + (self.Bg * self.wG)'''
        self.Bi = (self.Be * self.wE) #fordi 100% EK finansiert så er (self.Bg * self.wG) = 0 
        self.wE = 1 #fordi 100% EK, ignen gjeld; bare EK --> 100% = 1
        self.Bi = self.Be * self.wE  # AKA: self.Bi = self.Be hvis 100% EK 
        return self.Bi
    
    def mer_info(self):
        '''
        - gjeldsgrad øker til 3 
        - lån med 4% rente 
        - ved gjeldsgrad 3 => Bg = 0.1 
        '''
        #self.GE = self.G/self.E 
        self.GE = 3 
        self.Bg = 0.1 
        self.lånerente = 0.04 

    @property
    def E(self):
        ''' Se def G(self) for mer info '''
        self.E = 1 
        return self.E 
    
    @property
    def G(self):
        ''' siden GE = 3 må G være 3x større enn E
            siden vi ikke vet eksakt hva E og G er så setter vi E og G = brøktallene i den enkleste brøken:

            GE = 3 / 1 = 3 ==> G = 3 og E = 1  
        '''
        self.G = self.GE/self.E
        return self.E    
    
    def c(self):
        #Be = self.Bu + (self.G/self.E)*(self.Bu+self.Bg)
        self.Be = self.Bu + (self.GE*(self.Bu+self.Bg))
        return self.Be 