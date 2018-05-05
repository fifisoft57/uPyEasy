# Autogenerated file
def render(info, plugindata):
    yield """
<!- DO NOT CHANGE LINE ABOVE! -->
<TR>
   <TD>I2C Address:
   <TD>
      <select name='ssd_i2c'>
         <option value=60 """
    if plugindata['ssd_i2c'] == 60:
        yield """selected"""
    yield """>0x3C - (default)</option>
         <option value=61 """
    if plugindata['ssd_i2c'] == 61:
        yield """selected"""
    yield """>0x3D</option>
      </select>
<TR>
   <TD>
   <TD>
      <div class='note'>Note: SDO Low=0x3C, High=0x3D</div>
<TR>
   <TD>Rotation:
   <TD><input type='number' name='ssd_rotation' style='width:5em;' value="""
    yield str(plugindata['ssd_rotation'])
    yield """>
<TR>
 <TD>Display Size:
 <TD>
    <select name='ssd_size'>
       <option value=128 """
    if plugindata['ssd_size'] == 128:
        yield """selected"""
    yield """>128x64</option>
       <option value=64 """
    if plugindata['ssd_size'] == 64:
        yield """selected"""
    yield """>64x48</option>
    </select>
<TR>
 <TD>Line 1:
 <TD><input type='text' name='ssd_line1' maxlength='64' value='"""
    yield str(plugindata['ssd_line1'])
    yield """'>
<TR>
 <TD>Line 2:
 <TD><input type='text' name='ssd_line2' maxlength='64' value='"""
    yield str(plugindata['ssd_line2'])
    yield """'>
<TR>
 <TD>Line 3:
 <TD><input type='text' name='ssd_line3' maxlength='64' value='"""
    yield str(plugindata['ssd_line3'])
    yield """'>
<TR>
 <TD>Line 4:
 <TD><input type='text' name='ssd_line4' maxlength='64' value='"""
    yield str(plugindata['ssd_line4'])
    yield """'>
<TR>
 <TD>Line 5:
 <TD><input type='text' name='ssd_line5' maxlength='64' value='"""
    yield str(plugindata['ssd_line5'])
    yield """'>
<TR>
 <TD>Line 6:
 <TD><input type='text' name='ssd_line6' maxlength='64' value='"""
    yield str(plugindata['ssd_line6'])
    yield """'>
<TR>
 <TD>Line 7:
 <TD><input type='text' name='ssd_line7' maxlength='64' value='"""
    yield str(plugindata['ssd_line7'])
    yield """'>
<TR>
 <TD>Line 8:
 <TD><input type='text' name='ssd_line8' maxlength='64' value='"""
    yield str(plugindata['ssd_line8'])
    yield """'>
<TR>
 <TD>Display Timeout:
 <TD><input type='number' name='sss_timeout' style='width: 80px;' value='"""
    yield str(plugindata['ssd_timeout'])
    yield """'> (sec)
"""
    yield str(plugindata['content'])