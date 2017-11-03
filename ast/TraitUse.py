class TraitUse(Node):
    
    def __init__(self, kind, traits, adaptations):
        super().__init__(kind)
        self.traits = traits
        self.adaptations = adaptations