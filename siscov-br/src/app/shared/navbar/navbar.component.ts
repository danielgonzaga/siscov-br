import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  toggleSideMenu: boolean = false;

  abrir() {
    this.toggleSideMenu = !this.toggleSideMenu;
    console.log("toggleSideMenu: ", this.toggleSideMenu);
  }

}
