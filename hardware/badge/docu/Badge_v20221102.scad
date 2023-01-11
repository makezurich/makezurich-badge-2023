// CC BY-SA 4.0, MakeZurich.ch

$fn = 180;

// breadboard size
bbd_w = 81;
bbd_h = 51;

// AP9 box size
box_w = 77;
box_h = 77;
holes_w = 67;
holes_h = 33.5;
holes_r = 1.6;

// pico size
mcu_w = 21;
mcu_h = 51.3;
mcu_z = 3.9;

// badge size
// like breadboard
// but still fits in box
bdg_w = min(box_w, bbd_w);
bdg_h = max(min(box_h, bbd_h), mcu_h);

module base() {
  hull() {
    translate([6, 6]) {
      translate([0, 0]) {
        cylinder(1, 6, 6);
      }
      translate([bdg_w - 2 * 6, 0]) {
        cylinder(1, 6, 6);
      }
      translate([bdg_w - 2 * 6, bdg_h - 2 * 6]) {
        cylinder(1, 6, 6);
      }
      translate([0, bdg_h - 2 * 6]) {
        cylinder(1, 6, 6);
      }
    }
  }
}

module base_w_holes(){
    difference(){
        base();
        #translate([5,5,0]){
            cylinder(2,r=holes_r,center=true);
        };
        #translate([5+holes_w,5,0]){
            cylinder(2,r=holes_r,center=true);
        };        
        #translate([5,5+holes_h,0]){
            cylinder(2,r=holes_r,center=true);
        };        
        #translate([5+holes_w,5+holes_h,0]){
            cylinder(2,r=holes_r,center=true);
        };
    }
}

// board
//base_w_holes();

// translate([box_w - mcu_w - 10, 0, 1]) {
//  cube([mcu_w, mcu_h, mcu_z]);
//}

// cover
//translate([0, 0, 10]) base();

// dxf or svg export
//