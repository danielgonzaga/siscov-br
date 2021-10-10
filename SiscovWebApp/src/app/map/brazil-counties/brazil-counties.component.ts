import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-brazil-counties',
  templateUrl: './brazil-counties.component.html',
  styleUrls: ['./brazil-counties.component.css']
})
export class BrazilCountiesComponent implements OnInit {

  stateId = +this.route.snapshot.params.id;

  constructor(private route: ActivatedRoute) {
  }

  ngOnInit(): void {
  }

}
