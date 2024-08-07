# cmake file for DCF2024 Badge.
#set(MICROPY_HW_ENABLE_DOUBLE_TAP 1)
set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)

# The DCFurs Badges are not in upstream pico-sdk, so define it here.
list(APPEND PICO_BOARD_HEADER_DIRS ${MICROPY_BOARD_DIR})


