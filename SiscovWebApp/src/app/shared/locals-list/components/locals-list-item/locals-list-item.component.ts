import { Component, ElementRef, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-locals-list-item',
  templateUrl: './locals-list-item.component.html',
  styleUrls: ['./locals-list-item.component.css']
})
export class LocalsListItemComponent implements OnInit {

  @Input() item;

  constructor(private router: Router, private elRef: ElementRef) { }

  ngOnInit(): void {
  }

  goStatesMap() {
    this.router.navigateByUrl('/states');
  }

  goCountiesMap(stateId) {
    this.router.navigateByUrl('/states/' + stateId);
  }

  scrollIntoView() {
    this.elRef.nativeElement.scrollIntoView({behavior: 'smooth'});
  }
}
