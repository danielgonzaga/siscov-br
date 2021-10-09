import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TocantinsComponent } from './tocantins.component';

describe('TocantinsComponent', () => {
  let component: TocantinsComponent;
  let fixture: ComponentFixture<TocantinsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TocantinsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TocantinsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
