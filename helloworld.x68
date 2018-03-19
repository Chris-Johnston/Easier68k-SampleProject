; Constants
CR  EQU     $0D
LF  EQU     $0A

start   ORG    $1000
        ; Output the prompt message
        LEA     MSG, A1 
        MOVE.B  #14, D0 
        TRAP    #15     

        ; halt
        MOVE.B  #9, D0
        TRAP    #15

MSG     DC.B    'This is some text', CR, LF, 0

        SIMHALT             ; halt simulator

        END start
