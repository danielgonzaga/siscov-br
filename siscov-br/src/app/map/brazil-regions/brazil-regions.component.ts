import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-brazil-regions',
  templateUrl: './brazil-regions.component.html',
  styleUrls: ['./brazil-regions.component.css']
})
export class BrazilRegionsComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  goStatesMap() {
    this.router.navigateByUrl('/states');
  }

}
