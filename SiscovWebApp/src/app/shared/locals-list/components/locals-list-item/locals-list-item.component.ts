import { Component, ElementRef, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-locals-list-item',
  templateUrl: './locals-list-item.component.html',
  styleUrls: ['./locals-list-item.component.css']
})
export class LocalsListItemComponent implements OnInit {

  @Input() item;
  @Output() onClickOpenNewsModal = new EventEmitter();

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

  openNewsModal() {
    this.onClickOpenNewsModal.emit(this.item);
  }
}
