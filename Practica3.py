from mininet.topo import Topo

class Practica3( Topo ):
 
 def __init__( self ):
    "Create Practica-3 topo."

    # Initialize topology
    Topo.__init__( self )

    # Add hosts and switches
    #Subnet 10.0.1.0/24
    h1 = self.addHost( 'h1' )
    h2 = self.addHost( 'h2' )
    h3 = self.addHost( 'h3' )
    s1 = self.addSwitch( 's1' )
    #Subnet 10.0.2.0/24
    h4 = self.addHost( 'h4' )
    h5 = self.addHost( 'h5' )
    h6 = self.addHost( 'h6' )
    s3 = self.addSwitch( 's3' )
    #Net 151.100.37.12
    h7 = self.addHost( 'h7' )
    s2 = self.addSwitch( 's2' )

    # Add links
    #Subnet 10.0.1.0/24
    self.addLink( h1, s1 )
    self.addLink( h2, s1 )
    self.addLink( h3, s1 )
    #Subnet 10.0.2.0/24
    self.addLink( h4, s3 )
    self.addLink( h5, s3 )
    self.addLink( h6, s3 )
    #Net 151.100.37.12
    self.addLink( h7, s2 )

    #Switches connection
    self.addLink( s1, s2 )
    self.addLink( s3, s2 )

topos = { 'Practica3_Red': ( lambda: Practica3() ) }