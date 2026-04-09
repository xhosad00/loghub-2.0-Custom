From the postProcess options
   - DS (Double Space)
      - replace all consecutive spaces with `' '`
   - BL (Boolean) 
      - replace boolean with `<*>`
   - US (User String)
      - replace user strings with `<*>` (user strings are custom strings for this process)
   - DG (Digit)
      - replace digits `/^\d+$/` with `<*>` (the template was split by delimeters beforehand)
   - PS (Path-like String)
   - WV (Word concatenated with Variable)
      - replace words that are concatinated with variable `/^[^\s\/]*<\*>[^\s\/]*$/` with `<*>` (the template was split by delimeters beforehand)
   - DV (Dot-separated Variables)
      - replace `/<\*>\.<\*>/` with `<*>`
   - CV (Consecutive Variables)
      - join two variables that have no char between (so join `<*><*>` into `<*>`)
      - join two variables that are seperated by several delimeters (`/[#:/@.]/`)

The following were aplied
   - DS (Double Space)
   - DG (Digit)
   - WV (Word concatenated with Variable)
   - DV (Dot-separated Variables)
   - CV (Consecutive Variables)