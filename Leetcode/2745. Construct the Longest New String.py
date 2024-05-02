
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        
        @cache
        def create(currlen, leftx, lefty, leftz, last): # store = a,b,c
            if last=='AA' and lefty>0:
                return create(currlen+2, leftx, lefty-1, leftz, 'BB')
            
            elif last=='BB':
                if leftx>0 and leftz>0:
                    return max(
                        create(currlen+2, leftx-1, lefty, leftz, 'AA'), 
                        create(currlen+2, leftx, lefty, leftz-1, 'AB')
                                )
                elif leftx>0:
                    return create(currlen+2, leftx-1, lefty, leftz, 'AA')
                elif leftz >0:
                    return create(currlen+2, leftx, lefty, leftz-1, 'AB')
                else:
                    return currlen
                
            elif last=='AB':
                if leftx>0 and leftz>0:
                    return max(
                        create(currlen+2, leftx-1, lefty, leftz,'AA'),
                        create(currlen+2, leftx, lefty, leftz-1, 'AB')
                    )
                elif leftx>0:
                    return create(currlen+2, leftx-1, lefty, leftz,'AA')
                elif leftz>0:
                    return create(currlen+2, leftx, lefty, leftz-1, 'AB')
                else:
                    return currlen


            return currlen

        return max(
            create(2, x-1, y,z,'AA'),
            create(2,x,y-1,z, 'BB'),
            create(2, x,y,z-1, 'AB')
        )