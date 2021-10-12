import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-parana',
  templateUrl: './parana.component.html',
  styleUrls: ['./parana.component.css']
})
export class ParanaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
