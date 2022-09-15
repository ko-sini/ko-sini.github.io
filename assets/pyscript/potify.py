"""Compute angles in the top of the pot, or the "base" of a triangle
extended from the pot

      diameter_top
    _______________ 
    \      |      /
     \     |     /   height
      \    |    /
       \___|___/
      diameter_base

The volume of the pot is computed via an isosceles triangle for which
isosceles_height = <height (of pot)> + <height of "small cone">.
              _______________ 
              \ beta |  beta/                        
               \     |     /
                \    |    /  height (of pot)
  "big cone"     \___|___/ 
                  \  |  / 
                   \ | /  height of "small cone"
                    \|/
                   alpha

Steps:
    A) Compute alpha
        1. Compute beta by constructing an orthogonal triangle and computing tan(beta)
        using diameter_top_segment and height.
        2. Compute alpha
    B) Compute height of small cone
        3. Compute height of "small cone" with tan(alpha)
    C) Compute volume
        4. Compute volumes of "small cone" and "big cone" and finally the pot
"""

import numpy as np


RAD_180 = np.pi / 2


def compute_angles(
    diameter_top: float,
    diameter_base: float,
    height: float,
) -> tuple:
    """Compute alpha and beta in radians.

     beta ______________ beta
          \            /
           \          /
            \        /
             \______/
              \    /
               \  /
                \/
              alpha

    Args:
        diameter_top: Diameter measured from the top of the pot.
        diameter_base: Diameter measured from the base of the pot.
        height: Height of the pot

    Returns:
        Alpha and beta in radians.
    """
    # Compute beta
    width = (diameter_top - diameter_base) / 2
    tan_beta = height / width
    beta = np.arctan(tan_beta)
    # Compute alpha
    alpha = RAD_180 - 2 * beta 
    return alpha, beta


def v_cone(
    ray: float,
    height: float,
):
    return (np.pi * ray**2 * height) / 3


def v_pot(
    diameter_base: float,
    diameter_top: float,
    height: float,
):
    """Compute volume of the pot.

     _______________ 
     \             /
      \           /
       \         /
        \_______/
         \  |  /
          \ | /  height of "small cone"
           \|/

    Args:
        diameter_top: Diameter measured from the top of the pot.
        diameter_base: Diameter measured from the base of the pot.
        height: Height of the pot

    Returns:
        Volume of the pot
    """
    # A) Compute alpha
    alpha, _ = compute_angles(
        diameter_base=diameter_base, 
        diameter_top=diameter_top, 
        height=height
    )
    # B) Compute height of "small cone" and big cone
    h_small_cone = (diameter_base / 2) / np.tan(alpha)
    h_big_cone = height + h_small_cone
    # C) Compute volume
    v_small_cone = v_cone(ray=diameter_base/2, height=h_small_cone)
    v_big_cone = v_cone(ray=diameter_top/2, height=h_big_cone)
    return v_big_cone - v_small_cone


# if __name__ == "__main__":
#     v1 = v_pot(
#         diameter_base=11,
#         diameter_top=19,
#         height=18,
#     )
#     print("Volume of the pot is {} cm3".format(v1))
#     v2 = v_pot(
#         diameter_base=17,
#         diameter_top=18,
#         height=16,
#     )
#     print("Volume of the pot is {} cm3".format(v2))
#     print("Difference in volume is {} cm3".format(np.abs(v1-v2)))

#     # If optimal pot size is 2-4 inches larger in diameter than the roots of the plant...
#     #   1) ...how much is that in volume?
#     #   2) ...which pot should you choose? Or should you get a bigger pot?