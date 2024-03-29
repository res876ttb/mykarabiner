# mykarabiner

- karabiner_caps_lock_modifier.json
  - After importing this complex rules, you can freely enable/disable each of the rule. Just choose the one you would like to use.
  - Rule 1: Caps Lock Modifiers
    - This config is for karabiner on macOS, which makes capslock as a modifier
    - These shortcuts also work with other modifiers like command/shift/options/shift
    - Input method switch function will ***NOT*** work
    - The original function of turning on capslock will ***NOT*** work
    - Mapping `capslock + ikjl/wsad` to `arrow keys up/down/left/right`
    - Mapping `capslock + hn` to `backspace/delete` keys
    - Mapping `capslock + m,/zx` to `home/end` keys
    - Mapping `capslock + uo/qe` to `page up/down` keys
  - Rule 2: ctrl+shift modifier
    - Mapping `left_ctrl + shift` to `command + spacebar`
    - Mapping `fn + shift` to `command + spacebar`
  - Rule 3: right shift modifier
    - Mapping `right_shift` to `command + space`
    - This modifier is disabled in VMware Horizon Client, or the right shift will not work in VDI.
  - References
    - https://genesy.github.io/karabiner-complex-rules-generator/
      - Copy content in this json file to the website, and click install to install it
    - https://github.com/pqrs-org/Karabiner-Elements/issues/3120
      - The original method was posted in this github page, very thankful :)
    - https://github.com/yqrashawn/GokuRakuJoudo/blob/master/src/karabiner_configurator/keys_info.clj
      - All karabiner keycode can be found in this page
