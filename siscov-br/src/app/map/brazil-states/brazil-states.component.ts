import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-brazil-states',
  templateUrl: './brazil-states.component.html',
  styleUrls: ['./brazil-states.component.css']
})
export class BrazilStatesComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  goRegionsMap() {
    this.router.navigateByUrl('/regions');
  }

}
