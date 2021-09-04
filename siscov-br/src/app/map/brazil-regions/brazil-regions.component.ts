import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ILocalsItem } from 'src/app/shared/locals-list/locals-list.component';

@Component({
  selector: 'app-brazil-regions',
  templateUrl: './brazil-regions.component.html',
  styleUrls: ['./brazil-regions.component.css']
})
export class BrazilRegionsComponent implements OnInit {

  regions: ILocalsItem[] = [
    {name: 'Norte', isRegion: true, isState: false, isCounty: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Nordeste', isRegion: true, isState: false, isCounty: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Centro-Oeste', isRegion: true, isState: false, isCounty: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Sudeste', isRegion: true, isState: false, isCounty: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Sul', isRegion: true, isState: false, isCounty: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  ]

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  goStatesMap() {
    this.router.navigateByUrl('/states');
  }

}
